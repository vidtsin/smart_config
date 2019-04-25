# -*- coding: utf-8 -*-
from odoo import http

# class HhImplement(http.Controller):
#     @http.route('/hh_implement/hh_implement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hh_implement/hh_implement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hh_implement.listing', {
#             'root': '/hh_implement/hh_implement',
#             'objects': http.request.env['hh_implement.hh_implement'].search([]),
#         })

#     @http.route('/hh_implement/hh_implement/objects/<model("hh_implement.hh_implement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hh_implement.object', {
#             'object': obj
#         })