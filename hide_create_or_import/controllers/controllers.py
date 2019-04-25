# -*- coding: utf-8 -*-
from odoo import http

# class HideCreateBtnOnly(http.Controller):
#     @http.route('/hide_create_btn_only/hide_create_btn_only/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_create_btn_only/hide_create_btn_only/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_create_btn_only.listing', {
#             'root': '/hide_create_btn_only/hide_create_btn_only',
#             'objects': http.request.env['hide_create_btn_only.hide_create_btn_only'].search([]),
#         })

#     @http.route('/hide_create_btn_only/hide_create_btn_only/objects/<model("hide_create_btn_only.hide_create_btn_only"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_create_btn_only.object', {
#             'object': obj
#         })