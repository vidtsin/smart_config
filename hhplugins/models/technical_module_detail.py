# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64


class hhpluginsCheckboxRemoverDetail(models.Model):
    _name = 'hhplugins.checkbox.remover.detail'


class hhpluginsDynamicActionMenuDetail(models.Model):
    _name = 'hhplugins.dynamic.action.menu.detail'


class hhpluginsHideCreateImportButtonDetail(models.Model):
    _name = 'hhplugins.hide.create.import.button.detail'


class hhpluginsCompanyLogoCustomize(models.Model):
    _name = 'hhplugins.company.logo.customize'
    _inherit = 'ir.attachment'

    name = fields.Char('Attachment Name', required=True, default='Company Logo', readonly=True)
    res_model = fields.Char('Resource Model', readonly=True, default='hhplugins.company.logo.customize',
                            help="The database object this attachment will be attached to.")

    @api.model
    def create(self, vals):
        history_img = self.env['hhplugins.company.logo.customize'].search([])
        if len(history_img) > 0:
            history_img.unlink()

        image = open('.\\addons\hhplugins\static\img\logo.png', 'wb')
        image.write(base64.b64decode(vals['datas']))
        res = super(hhpluginsCompanyLogoCustomize, self).create(vals)
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload',
        # }
        return res

