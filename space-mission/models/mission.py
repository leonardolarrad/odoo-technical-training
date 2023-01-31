# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'space_mission.mission'
    _description = 'Space Mission'

    name = fields.Char(
        string="Nombre", 
        required=True
    )

    spaceship_id = fields.Many2one(
        comodel_name='space_mission.spaceship', 
        string="Nave Espacial", 
        required=True
    )

    commander_id = fields.Many2one(
        comodel_name='res.partner',
        string="Comandante",
        required=True
    )

    launch_date = fields.Date(string="Fecha de lanzamiento", required=True)
    arrival_date = fields.Date(string="Fecha de llegada", required=True)

    fuel_consumption = fields.Float(
        string="Consumo de combustible"
    )

    cost = fields.Monetary(string="Costo", default=0.00)

    crew_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Tripulación",
    )

    