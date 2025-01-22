# -*- coding: utf-8 -*-
{
    'name': "Gym Management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Gym Management 
    """,

    'author': "Manar Braham",
    'website': "https://www.gym.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/gym_client_view.xml",
        "views/menu.xml",
         "views/gym_trainer_view.xml",
        "views/gym_paiement_view.xml",
        "views/gym_session_view.xml",

    ],
    'installable': True,
    'application': True,
}

