# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Cursos Académicos'

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    level = fields.Selection([
        ('beginner', 'Principiante'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
    ], string="Nivel", copy=False)
    
    active = fields.Boolean(
        string='Activo', 
        default=True
    )

    base_price = fields.Float(string="Precio Base", default=0.00)
    additional_fee = fields.Float(string="Comisión Adicional", default=10.00)
    
    total_price = fields.Float(
        string="Precio Total", 
        readonly=True, 
        compute='_compute_total_price', 
        store=True
    )
    
    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.base_price + record.additional_fee

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0 or self.additional_fee < 0:
            raise UserError("El precio base y la comisión adicional no pueden ser negativos.")

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError("La comisión adicional no puede ser menor a 10.00.")