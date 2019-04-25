# -*- coding: utf-8 -*-
{
    'name': "Toppwork Customize User Menu",
    'version': '11.0',
    'summary': """
            Customize drop down user menu.""",
    'description': """
            Customize drop down user menu.
        """,
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    "external_dependencies": {"python": [], "bin": []},
    'depends': ['base', 'web'],
    'images': [
        'static/description/icon.png'
    ],
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