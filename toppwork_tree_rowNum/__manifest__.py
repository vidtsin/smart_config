# -*- encoding: utf-8 -*-
{
    'name': "Toppwork Tree Row Num",
    'version': '11.0',
    'summary': """
            Adds a column which shows row number on the List/Tree view.""",
    'description': """
            Adds a column which shows row number on the List/Tree view.
        """,
    'website': "http://www.toppwork.com",
    'category': 'Productivity',
    'license': 'LGPL-3',
    "external_dependencies": {"python": [], "bin": []},
    "depends": ['web'],
    "live_test_url": "https://odoo.sheliyainfotech.com/contactus?description=demo:rowno_in_tree&odoo_version=12.0",
    'data': [
             'views/listview_templates.xml',
             ],
    "images": ["static/description/screen1.png"],
    'qweb': [
            ],  
    
    'installable': True,
    'application': False,
    'auto_install': False,
}
