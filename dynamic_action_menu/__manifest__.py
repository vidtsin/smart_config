# -*- coding: utf-8 -*-
{
    'name': "Action Menu Filter",

    'summary': """
        Custom pick any action menu items you need for each page """,

    'description': """
       
    """,

    'author': "HungHing -- Toppwork",
    'website': "http://www.hunghingprinting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0',
    "external_dependencies": {"python": [], "bin": []},

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}