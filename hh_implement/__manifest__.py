# -*- coding: utf-8 -*-
{
    'name': "HH layout",

    'summary': """
        Module for Hung Hing Implementation""",

    'description': """
        1. Customize login page (views.xml)
            1.1 Added Hung Hing logo
            1.2 Removed 'Manage Database and Powered by Odoo' footer
        2. Customize main page dashboard (custom_base_user_menu.xml)
            2.1 Hide Discuss & Employee App on dashboard
            2.2 Hide unnecessary menu option under user's name
            2.3 Hide 2 button besides user name
    """,

    'author': "HungHing -- Toppwork",
    'website': "http://www.hunghingprinting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'hr'],

    'qweb': [
        # 'static/src/xml/*.xml',
        # 'static/src/xml/custom_base_user_menu.xml',
        # # 'static/src/xml/base.xml',
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}