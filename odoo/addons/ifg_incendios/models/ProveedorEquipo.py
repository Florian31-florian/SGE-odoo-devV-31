

 from odoo import models, fields, api


class model.technical.name(models.Model):
    _name = 'ifg_incendios.proveedor'
    _description = 'Proveedor'

    name = fields.Char('Nombre del proveedor',required=True)
    field_name = fields.Selection([
        ('venta', 'Venta de equipos'),
        ('mantenimiento','Mantenimiento de equipos')
    ], string='Tipo de Servicio',required=True)
    telefono = fields.Char('Teléfono')
    direccion = fields.Char('Dirección')
    correo = fields.Char('Correo electrónico')