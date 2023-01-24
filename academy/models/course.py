# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Cursos Académicos'

    title = fields.Char(string="Título", required=True)
    description = fields.Text()
    level = fields.Selection([
        ('beginner', 'Principiante'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
    ], copy=False)

    active = fields.Boolean(string='Activo', default=True)