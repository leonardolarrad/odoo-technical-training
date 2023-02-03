# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class Spaceship(models.Model):
    _name = 'space_mission.spaceship'
    _description = 'Spaceship to go to the moon and back'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Name", 
        required=True,
        tracking=True
    )
    description = fields.Text(
        string="Description",
        tracking=True
    )
        
    crew_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ],  string="Crew Size", 
        copy=False, 
        default='small',
        tracking=True
    )
    
    crew_capacity = fields.Integer(
        string="Crew Capacity",
        default=0,
        tracking=True
    )

    fuel = fields.Char(
        string="Fuel", 
        default='Plutonium-238',
        tracking=True
    )

    fuel_capacity = fields.Integer(
        string="Fuel Capacity", 
        default=0,
        tracking=True
    )

    width = fields.Float(
        string="Width",
        default=0.00,
        tracking=True
    )

    height = fields.Float(
        string="Height",
        default=0.00,
        tracking=True
    )

    mission_ids = fields.One2many(
        comodel_name='space_mission.mission',
        inverse_name='spaceship_id',
        string="Missions",
        tracking=True
    )

    @api.constrains('width', 'height')
    def _check_dimensions(self):
        for record in self:
            if record.width < 0 or record.height < 0:
                raise ValidationError(_("Dimensions (width & height) cannot be negative"))

            if record.width > record.height:
                raise UserError(_("Width cannot be greater than height"))

    active = fields.Boolean(string='Active', default=True)