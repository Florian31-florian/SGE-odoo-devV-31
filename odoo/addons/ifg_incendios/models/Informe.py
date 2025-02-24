from odoo import models,EquipoContraIncendios, fields, api



class Informe(models.Model):
    _name = 'ifg_incendios.informe'
    _description = 'ifg_incendios.Informes de inspección de equipos contra incendios'

    equipo_id= fields.Many2one('ifg_incendios.equipo', string='Equipo', required=True)
    fecha_inspeccion = fields.Date(string='Fecha de inspección', required=True)
    inspector = fields.Char(string='Inspector', required=True)
    estado = fields.Selection([
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
        ('reparacion', 'Reparación necesaria')
    ], string='Estado', required=True)
    observaciones = fields.Text(string='Observaciones')