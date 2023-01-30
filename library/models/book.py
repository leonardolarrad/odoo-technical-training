# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    isbn = fields.Char(string="ISBN")
    release_date = fields.Date(string="Fecha de publicación")
    author = fields.Char(string="Autor")
    genre = fields.Selection([
        ('fiction', 'Ficción'),
        ('nonfiction', 'No-ficción'),
        ('biography', 'Biografía'),
        ('poetry', 'Poesía'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasía'),
        ('science_fiction', 'Ciencia Ficción'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('mystery', 'Misterio'),
        ('crime', 'Crimen'),
        ('history', 'Historia'),
        ('self_help', 'Autoayuda'),
        ('health', 'Salud'),
        ('guide', 'Guía'),
        ('travel', 'Viajes'),
        ('children', 'Infantil'),
        ('religion', 'Religión'),
        ('science', 'Ciencia'),
        ('math', 'Matemáticas'),
        ('philosophy', 'Filosofía'),
        ('social_science', 'Ciencias Sociales'),
        ('language', 'Idiomas'),
        ('art', 'Arte'),
        ('cooking', 'Cocina'),
        ('novel', 'Novela'),
        ('comics', 'Cómics'),
        ('graphic_novel', 'Novela Gráfica'),
        ('other', 'Otro'),
    ], string="Género", default='fiction')
    
    active = fields.Boolean(string='Activo', default=True)