# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Spaceship(models.Model):
    _name = 'space_mission.spaceship'
    _description = 'Spaceship to go to the moon and back'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
        
    crew_size = fields.Selection([
        ('small', 'Pequeño'),
        ('medium', 'Mediano'),
        ('large', 'Grande'),
    ],  string="Capacidad de tripulación", 
        copy=False, 
        default='small'
    )
    
    crew_capacity = fields.Integer(
        string="Tamaño del equipo", 
        default=0
    )

    fuel = fields.Char(
        string="Combustible", 
        default='Plutonio-238'
    )

    fuel_capacity = fields.Integer(
        string="Capacidad de combustible", 
        default=0
    )

    width = fields.Float(
        string="Ancho",
        default=0.00
    )

    height = fields.Float(
        string="Alto",
        default=0.00
    )

    @api.constrains('width', 'height')
    def _check_dimensions(self):
        for record in self:
            if record.width < 0 or record.height < 0:
                raise ValidationError("Las dimensiones (ancho) y (alto) no pueden ser negativas")

            if record.width > record.height:
                raise UserError("El ancho no puede ser mayor que el alto")

    active = fields.Boolean(string='Activa', default=True)