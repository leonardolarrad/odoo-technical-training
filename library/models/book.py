# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    isbn = fields.Char(string="ISBN")
    date_release = fields.Date(string="Fecha de publicación")
    author = fields.Char(string="Autor")
    genre = fields.Selection([
        ('fiction', 'Ficción'),
        ('nonfiction', 'No ficción'),
        ('biography', 'Biografía'),
        ('poetry', 'Poesía'),
        ('drama', 'Drama'),
        ('other', 'Otro'),
    ], string="Género", copy=False)
    
    active = fields.Boolean(string='Activo', default=True)