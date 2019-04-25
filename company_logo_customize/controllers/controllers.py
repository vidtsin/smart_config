# -*- coding: utf-8 -*-
from odoo import http

# class CompanyLogoCustomize(http.Controller):
#     @http.route('/company_logo_customize/company_logo_customize/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_logo_customize/company_logo_customize/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_logo_customize.listing', {
#             'root': '/company_logo_customize/company_logo_customize',
#             'objects': http.request.env['company_logo_customize.company_logo_customize'].search([]),
#         })

#     @http.route('/company_logo_customize/company_logo_customize/objects/<model("company_logo_customize.company_logo_customize"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_logo_customize.object', {
#             'object': obj
#         })