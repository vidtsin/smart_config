# -*- coding: utf-8 -*-
{
    'name': "Smart Plugins",
    'version': '1.0',
    'sequence': 1,
    'summary': """
        A collection of modules built to enhance the overall usability 
        and simple customizations to Odoo List/Tree views.
    """,
    'description': """
        A collection of modules built to enhance the overall usability 
        and simple customizations to Odoo List/Tree views.
    """,
    'author': "Toppwork",
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base'],
    'images': ['images/hhplugins_screenshot.jpg'],
    'data': [
        'security/hhplugins_security.xml',
        'security/ir.model.access.csv',
        'views/hh_module_config.xml',
        'views/templates.xml',
        'views/test.xml',
        'views/checkbox_remover_detail.xml',
        'views/dynamic_action_menu_detail.xml',
        'views/hide_create_or_import_btn_detail.xml',
        'views/company_logo_customize.xml',
    ],
    'price': 9.9,
    'currency': 'EUR',
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
