# # -*- coding: utf-8 -*-
# from odoo import http
# import werkzeug
# from odoo.http import request
# import base64
#
#
# class hhpluginsBinary(http.Controller):
#     @http.route('/web/binary/hhplugins/logo', type='http', auth='public')
#     def make_response_for_hhplugins(self, **kwargs):
#         db_path = '.\\addons\hhplugins\static\img\logo.png'
#         data = base64.b64decode(db_path)
#         # file_title = file_name.split('(')[0] + '.' + file_name.split('.')[1]
#         file_title = 'Company_logo.png'
#         headers = werkzeug.datastructures.Headers()
#         headers.set('Content-Disposition', 'attachment', filename=file_title)
#         return request.make_response(data, headers)