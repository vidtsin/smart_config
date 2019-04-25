# -*- coding: utf-8 -*-
{
    'name': "Toppwork Hide Form Button",
    'version': '11.0',
    'summary': """
            Hides the Create and/or the Import button on the List/Tree view on demand.""",
    'description': """
            Hides the Create and/or the Import button on the List/Tree view on demand.
        """,
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    "external_dependencies": {"python": [], "bin": []},
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