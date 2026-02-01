# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL


class PortalInventoryController(http.Controller):

    def _get_earliest_incoming_eta_map(self, product_ids):
        if not product_ids:
            return {}
        moves = request.env['stock.move'].sudo().search([
            ('product_id', 'in', product_ids),
            ('state', 'in', ['waiting', 'confirmed', 'assigned']),
            ('location_dest_id.usage', '=', 'internal'),
        ], order='date asc')
        eta_map = {}
        for m in moves:
            pid = m.product_id.id
            if pid in eta_map:
                continue
            if m.date:
                eta_map[pid] = fields.Date.to_string(m.date.date())
            else:
                eta_map[pid] = ''
        return eta_map

    @http.route(['/my/inventory', '/my/inventory/page/<int:page>'], type='http', auth='user', website=True,
                sitemap=False)
    def portal_inventory(self, page=1, category_id=None, search=None, **kw):
        category = request.env['product.category'].sudo()
        product = request.env['product.template'].sudo()
        root_categs = category.search([('parent_id', '=', False)], order="complete_name")
        selected_category = category.browse(int(category_id)) if category_id else category.browse()
        domain = [('active', '=', True)]
        if category_id:
            domain += [('categ_id', 'child_of', int(category_id))]
        if search:
            s = (search or "").strip()
            domain += ['|',
                       ('name', 'ilike', s),
                       ('default_code', 'ilike', s)]
        # Pagination
        page_size = 10
        total = product.search_count(domain)
        pager = request.website.pager(
            url="/my/inventory",
            total=total,
            page=page,
            step=page_size,
            url_args={"category_id": category_id, "search": search},
        )
        templates = product.search(domain, limit=page_size, offset=pager['offset'], order="name")
        variant_ids = templates.mapped('product_variant_id').ids
        eta_map = self._get_earliest_incoming_eta_map(variant_ids)
        products_data = []
        for t in templates:
            p = t.product_variant_id
            products_data.append({
                "template_id": t.id,
                "variant_id": p.id,
                "name": t.name,
                "default_code": p.default_code or t.default_code or "",
                "qty_on_hand": p.qty_available,  # On Hand
                "forecast_qty": p.virtual_available,  # Forecast
                "forecast_eta": eta_map.get(p.id, ""),
                "category": t.categ_id.complete_name if t.categ_id else "",
            })
        keep = QueryURL('/my/inventory', category_id=category_id, search=search)
        values = {
            "root_categs": root_categs,
            "selected_category_id": int(category_id) if category_id else False,
            "selected_category": selected_category,
            "search": search or "",
            "products": products_data,
            "pager": pager,
            "keep": keep,
        }
        return request.render("inventory_portal_for_customer.portal_inventory_page", values)
