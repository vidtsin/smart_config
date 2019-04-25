# -*- coding: utf-8 -*-
{
    'name': "Toppwork Action Menu Filter",
    'version': '11.0',
    'summary': """
            Customize Action Items under the Action dropdown menu. Line separators are also available from this module.
            """,
    'description': """
            Customize Action Items under the Action dropdown menu. Line separators are also available from this module.
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