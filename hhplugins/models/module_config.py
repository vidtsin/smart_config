# -*- coding: utf-8 -*-
from odoo import models, api, fields
from shutil import copyfile


class HHModuleConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    toppwork_dynamic_list = fields.Boolean('Dynamic List View', default=False, store=True)
    toppwork_record_highlighted = fields.Boolean('Record Highlight', default=False, store=True)
    toppwork_tree_rowNum = fields.Boolean('Row Number', default=False, store=True)
    company_logo_customize = fields.Boolean('Company Logo', default=False, store=True)

    checkbox_remover = fields.Boolean('Checkbox Remover', default=False, store=True)
    dynamic_action_menu = fields.Boolean('Dynamic Action Menu', default=False, store=True)
    hide_create_or_import = fields.Boolean('Hide Create/Import Button', default=False, store=True)

    hh_implement = fields.Boolean('Customize User Menu', default=True, store=True)
    hh_implement_documentation = fields.Boolean('Hide Documentation', default=False, store=True)
    hh_implement_support = fields.Boolean('Hide Support', default=False, store=True)
    hh_implement_shortcuts = fields.Boolean('Hide Shortcuts', default=False, store=True)
    hh_implement_settings = fields.Boolean('Hide Preferences', default=False, store=True)
    hh_implement_account = fields.Boolean('Hide My Odoo.com account', default=False, store=True)

    test_string = fields.Char('Test String', default='Test String', store=True)

    @api.model
    def get_values(self):
        res = super(HHModuleConfig, self).get_values()
        res.update(
            toppwork_dynamic_list=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.toppwork_dynamic_list'),
            toppwork_record_highlighted=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.toppwork_record_highlighted'),
            toppwork_tree_rowNum=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.toppwork_tree_rowNum'),
            checkbox_remover=self.env['ir.config_parameter'].sudo().get_param(
                    'hhplugins.checkbox_remover'),
            dynamic_action_menu=self.env['ir.config_parameter'].sudo().get_param(
                    'hhplugins.dynamic_action_menu'),
            hide_create_or_import=self.env['ir.config_parameter'].sudo().get_param(
                    'hhplugins.hide_create_or_import'),

            hh_implement=self.env['ir.config_parameter'].sudo().get_param(
                    'hhplugins.hh_implement'),
            hh_implement_documentation=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.hh_implement_documentation'),
            hh_implement_support=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.hh_implement_support'),
            hh_implement_shortcuts=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.hh_implement_shortcuts'),
            hh_implement_settings=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.hh_implement_settings'),
            hh_implement_account=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.hh_implement_account'),
            # hh_implement_activity_icon=self.env['ir.config_parameter'].sudo().get_param(
            #     'hhplugins.hh_implement_activity_icon'),
            company_logo_customize=self.env['ir.config_parameter'].sudo().get_param(
                'hhplugins.company_logo_customize'),
            )
        return res

    @api.multi
    def set_values(self):
        super(HHModuleConfig, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.toppwork_dynamic_list',
                                                         self.toppwork_dynamic_list)
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.toppwork_record_highlighted',
                                                         self.toppwork_record_highlighted)
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.toppwork_tree_rowNum',
                                                         self.toppwork_tree_rowNum)
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.checkbox_remover',
                                                         self.checkbox_remover)
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.dynamic_action_menu',
                                                         self.dynamic_action_menu)
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hide_create_or_import',
                                                         self.hide_create_or_import),

        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement',
                                                         self.hh_implement),
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_documentation',
                                                         self.hh_implement_documentation if self.hh_implement else False),
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_support',
                                                         self.hh_implement_support if self.hh_implement else False),
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_shortcuts',
                                                         self.hh_implement_shortcuts if self.hh_implement else False),
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_settings',
                                                         self.hh_implement_settings if self.hh_implement else False),
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_account',
                                                         self.hh_implement_account if self.hh_implement else False),
        # self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_activity_icon',
        #                                                  self.hh_implement_activity_icon) if self.hh_implement else False,
        # self.env['ir.config_parameter'].sudo().set_param('hhplugins.hh_implement_message_icon',
        #                                                  self.hh_implement_message_icon) if self.hh_implement else False,
        self.env['ir.config_parameter'].sudo().set_param('hhplugins.company_logo_customize',
                                                         self.company_logo_customize)
        install_list = list()
        uninstall_list = list()
        install_list.append('toppwork_dynamic_list') if self.toppwork_dynamic_list else uninstall_list.append('toppwork_dynamic_list')
        install_list.append('toppwork_record_highlighted') if self.toppwork_record_highlighted else uninstall_list.append('toppwork_record_highlighted')
        install_list.append('toppwork_tree_rowNum') if self.toppwork_tree_rowNum else uninstall_list.append('toppwork_tree_rowNum')
        install_list.append('checkbox_remover') if self.checkbox_remover else uninstall_list.append('checkbox_remover')
        install_list.append('dynamic_action_menu') if self.dynamic_action_menu else uninstall_list.append('dynamic_action_menu')
        install_list.append('hide_create_or_import') if self.hide_create_or_import else uninstall_list.append('hide_create_or_import')
        install_list.append('hh_implement') if self.hh_implement else uninstall_list.append('hh_implement')
        install_list.append('company_logo_customize') if self.company_logo_customize else uninstall_list.append('company_logo_customize')

        module_to_install = self.env['ir.module.module'].sudo().search([('name', 'in', install_list),
                                                                        ('state', 'not in', ['installed', 'to install', 'to upgrade'])])

        if 'company_logo_customize' in uninstall_list:
            copyfile('.\\addons\hhplugins\static\img\default_logo\logo.png', '.\\addons\hhplugins\static\img\logo.png')

        module_to_uninstall = self.env['ir.module.module'].sudo().search([('name', 'in', uninstall_list),
                                                                        ('state', '!=', 'uninstalled')])

        module_to_install.button_immediate_install() if len(module_to_install) > 0 else False
        for module in module_to_uninstall:
            module.button_immediate_uninstall()

    def show_checkbox_remover_detail_page(self):
        # print('show_dynamic_action_menu_detail_page')
        view_ref = self.env.ref('hhplugins.hhplugins_checkbox_remover_detail_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_ref,
            'res_model': 'hhplugins.checkbox.remover.detail',
            # 'res_id': 1,
            'target': 'new',
            'hide_footer': True
        }

    def show_dynamic_action_menu_detail_page(self):
        # print('show_dynamic_action_menu_detail_page')
        view_ref = self.env.ref('hhplugins.hhplugins_dynamic_action_menu_detail_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_ref,
            'res_model': 'hhplugins.dynamic.action.menu.detail',
            # 'res_id': 1,
            'target': 'new',
            'hide_footer': True
        }

    def show_hide_create_or_import_btn_detail_page(self):
        # print('show_dynamic_action_menu_detail_page')
        view_ref = self.env.ref('hhplugins.hhplugins_hide_create_import_button_detail_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_ref,
            'res_model': 'hhplugins.hide.create.import.button.detail',
            # 'res_id': 1,
            'target': 'new',
            'hide_footer': True
        }

    def upload_company_logo(self):
        history_img = self.env['hhplugins.company.logo.customize'].search([])
        if len(history_img) > 0:
            history_img.unlink()
        view_ref = self.env.ref('hhplugins.view_document_file_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_ref,
            'res_model': 'hhplugins.company.logo.customize',
            # 'res_id': self.id,
            'target': 'new',
            # 'hide_footer': True
            # 'context': {
            #     'default_res_model': 'hhplugins.company.logo.customize',
            #     'default_res_id': self.id,
            # }
        }

    # def download_company_logo(self):
    #     print('aaaaaa')
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'target': 'self',
    #         'url': f'/web/binary/hhplugins/logo'
    #     }