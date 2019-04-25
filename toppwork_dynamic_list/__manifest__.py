# -*- coding: utf-8 -*-

{
    'name': 'Toppwork Dynamic List',
    'version': '11.0',
    "external_dependencies": {"python": [], "bin": []},
    'author': "Toppwork",
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    'summary': 'Show/Hide column(s) within a dropdown box on the List/Tree view.',
    'description': """

    Show/Hide column(s) within a dropdown box on the List/Tree view.

    """,
    'images': ['static/description/saleorders.png'
    ],
    'depends': ['web'],
    'data': [
    'views/listview_button.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': ['static/src/xml/listview_button_view.xml'],
}

