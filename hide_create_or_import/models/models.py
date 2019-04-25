# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class hide_create_btn_only(models.Model):
#     _name = 'hide_create_btn_only.hide_create_btn_only'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100