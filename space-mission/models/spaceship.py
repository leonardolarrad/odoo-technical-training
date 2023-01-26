# -*- coding: utf-8 -*-

from odoo import models, fields, api

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

    active = fields.Boolean(string='Activa', default=True)