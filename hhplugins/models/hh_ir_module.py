# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hhIrModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def button_immediate_uninstall(self):
        """
        Uninstall the selected module(s) immediately and fully,
        returns the next res.config action to execute
        """
        if self.name == 'hhplugins':
            uninstall_list = ['toppwork_dynamic_list', 'toppwork_tree_rowNum', 'toppwork_record_highlighted', 'hh_implement', 'company_logo_customize',
                              'checkbox_remover', 'dynamic_action_menu', 'hide_create_or_import']
            module_to_uninstall = self.env['ir.module.module'].sudo().search([('name', 'in', uninstall_list),
                                                                              ('state', '!=', 'uninstalled')])
            for module in module_to_uninstall:
                module.button_immediate_uninstall()

            for module in uninstall_list:
                module_name = 'hhplugins.' + module
                self.env['ir.config_parameter'].sudo().set_param(module_name, False)

        super(hhIrModule, self).button_immediate_uninstall()

