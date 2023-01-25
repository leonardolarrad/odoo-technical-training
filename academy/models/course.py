# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Cursos Académicos'

    name = fields.Char(string="Título", required=True)
    description = fields.Text()
    level = fields.Selection([
        ('beginner', 'Principiante'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
    ], string="Nivel", copy=False)

    active = fields.Boolean(string='Activo', default=True)