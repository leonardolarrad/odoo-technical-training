# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Academy Session'

    name = fields.Char(string='Name', required=True)
    
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

    students_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Estudiantes'
    )