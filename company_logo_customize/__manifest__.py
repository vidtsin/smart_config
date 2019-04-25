# -*- coding: utf-8 -*-
{
    'name': "Toppwork Customize Company Logo",
    'version': '11.0',
    'summary': """
            Use your own company logo instead of ODOO.""",
    'description': """
            Use your own company logo instead of ODOO.
        """,
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    "external_dependencies": {"python": [], "bin": []},
    'depends': ['base'],
    'images': [
        'static/description/icon.png'
    ],
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