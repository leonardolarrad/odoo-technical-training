# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProdcutTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean(
        string='Usar como producto',
        help="Marcar si la sesión se vende como un producto"
        default=False
    )