# -*- coding: utf-8 -*-
{
    'name': "student",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'sale_management'],

    # always loaded
    'data': [
        "data/student_school_record.xml",
        "security/ir.model.access.csv",
        "views/student_view.xml",
        "views/sale_order.xml",
        "views/sale_report_inherit.xml"
    ],
    'installable': True,
    'application': True,
}

