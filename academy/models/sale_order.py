# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    session_id = fields.Many2one(
        'academy.session', 
        string='Session', 
        ondelete='set null')

    intructor_id = fields.Many2one(
        string='Instructor de la sesión',
        related='session_id.instructor_id'
    )


    student_ids = fields.Many2many(
        string = 'Estudiantes',
        related='session_id.student_ids'
    )

