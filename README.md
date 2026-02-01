# MaplesHub – Inventory Portal for Customer (Odoo 19)

Inventory Portal for Customer is an Odoo module that allows customers to securely view product availability, stock levels, and forecast information directly from the Odoo portal — without requiring backend access.

It is designed as a **read-only inventory visibility tool** to improve customer experience, reduce manual inquiries, and keep internal inventory data protected.

---

## Key Features

- **Secure Portal Access**
  - Customers access inventory through the Odoo Portal
  - No backend or internal user permissions required
  - Read-only by design

- **Category-Based Product Navigation**
  - Expandable and collapsible category tree
  - Clean, catalog-style browsing experience
  - Parent categories remain expanded when viewing sub-categories

- **Smart Product Search**
  - Search by product name or description
  - Fast and responsive filtering

- **Real-Time Inventory Data**
  - Quantity On Hand
  - Forecasted Quantity
  - Expected Availability Date (ETA) based on incoming stock

- **Clean & User-Friendly UI**
  - Full-width clickable category rows
  - Modern, minimal design optimized for non-technical users
  - Compatible with standard Odoo Website themes

---

## Business Benefits

- Reduce repetitive stock availability inquiries
- Improve transparency with customers
- Save time for sales and operations teams
- Keep sensitive inventory data secure
- Enhance customer satisfaction through self-service access

---

## Ideal For

- Manufacturers  
- Distributors  
- Wholesalers  
- B2B businesses  
- Any company that wants to share inventory visibility with customers safely  

---

## Technical Overview

- Built using standard Odoo models:
  - `product.template`
  - `product.product`
  - `product.category`
  - `stock.move`
- Uses Odoo portal authentication (`auth="user"`)
- No changes to core inventory or sales workflows
- Lightweight and performance-friendly
- Compatible with **Odoo Community and Enterprise editions**

---

## Installation

1. Copy the module into your Odoo `addons` directory
2. Update the app list
3. Install **Inventory Portal for Customer**
4. Ensure customers have **Portal access**

---

## Configuration

- No mandatory configuration required

## Maintained By

**MaplesHub Solutions**  
🌐https://mapleshub.com/
