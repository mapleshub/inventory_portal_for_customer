{
    "name": "Inventory Portal for Customer",
    "version": "1.0",
    "category": "Website",
    "summary": "A secure, read-only inventory portal that allows customers to view product availability, "
               "stock levels, and forecast quantities directly from Odoo—without backend access.",
    "depends": ["website", "portal", "product", "stock"],
    "data": [
        "views/portal_inventory_templates.xml",
        "views/website_menu.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "inventory_portal_for_customer/static/src/css/portal_inventory.css",
        ],
    },
    "installable": True,
    "application": False,
    "license": 'LGPL-3',
    'description': """
    Inventory Portal for Customer is a customer-friendly Odoo module that extends the standard portal to provide 
    real-time inventory visibility in a clean, easy-to-use interface. Instead of responding to repeated stock 
    availability emails or sharing screenshots, businesses can now offer customers self-service access to product 
    availability—securely and efficiently.The module is designed specifically for non-technical portal users, ensuring 
    clarity, simplicity, and safety while keeping internal inventory operations fully protected.
    """,
}
