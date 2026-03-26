{
    "name": "Warehouse User Restriction",
    "version": "18.0.1.0.0",
    "summary": "Restrict warehouse-related records per user using record rules",
    "description": """
Production-ready warehouse access restriction module for Odoo 18.
Users can access only assigned warehouses and related stock records.

Author:   Haytham Afify
Email:    haythamgamal6@gmail.com
GitHub:   https://github.com/haythamafify
LinkedIn: https://www.linkedin.com/in/haytham-gamal-4165797a/
    """,
    "category": "Inventory",
    "author": "Haytham Afify",
    "maintainer": "Haytham Afify <haythamgamal6@gmail.com>",
    "website": "https://github.com/haythamafify",
    "license": "LGPL-3",
    "depends": ["stock"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_users_views.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
