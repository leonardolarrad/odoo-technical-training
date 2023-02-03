# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'space_mission.mission'
    _description = 'Space Mission'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Name", 
        required=True
    )

    spaceship_id = fields.Many2one(
        comodel_name='space_mission.spaceship', 
        string="Spaceship", 
        required=True
    )

    commander_id = fields.Many2one(
        comodel_name='res.partner',
        string="Commander",
        required=True,
        tracking=True
    )

    launch_date = fields.Date(
        string="Launch Date", 
        required=True,
        tracking=True
    )

    arrival_date = fields.Date(
        string="Arrival Date", 
        required=True,
        tracking=True
    )

    fuel_consumption = fields.Float(
        string="Fuel Consumption",
    )

    cost = fields.Monetary(
        string="Cost", 
        default=0.00,
        tracking=True
    )

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string="Currency",
        default=lambda self: self.env.user.company_id.currency_id.id
    )

    crew_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Crew",
    )

    