# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Academy Session'
    
    course_id = fields.Many2one(
        comodel_name='academy.course', 
        string='Curso', 
        required=True
    )

    name = fields.Char(
        string='Título', 
        related='course_id.name'
    )

    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Instructor'
    )

    student_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Estudiantes'
    )

    start_date = fields.Date(
        string='Fecha de Inicio'
    )

    duration = fields.Integer(
        string='Días de sesión', 
        default=1.00
    )

    end_date = fields.Date(
        string='Fecha de Finalización', 
        compute='_compute_end_date',
        inverse='_inverse_end_date',
        store=True
    )

    total_price = fields.Float(
        string="Precio Total",
        related='course_id.total_price'
    )

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
            

    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days
            else:
                continue