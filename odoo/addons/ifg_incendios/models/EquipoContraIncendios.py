from odoo import models, fields, api



class EquipoContraIncendios(models.Model):
    _name = 'ifg_incendios.equipo'
    _description = 'ifg_incendios.EquipoContraIncendios'

    name = fields.Char('Nombre del equipo',required=True)
    tipo_equipo = fields.Selection([
        ('extintor', 'Extintor'),
        ('hidrante', 'Hidrante'),
        ('manguera', 'Manguera'),
        ('detector', 'Detector'),
        ('pulsador', 'Pulsador'),
        ('rociador', 'Rociador'),
        ('sirena', 'Sirena'),
        ('central incendios', 'Central Incendios')
    ], string='Tipo de equipo', required=True)
    ubicacion = fields.Char('Ubicación')
    fecha_ultimo_mantenimiento = fields.Date('Última fecha de mantenimiento')
    fecha_proximo_mantenimiento = fields.Date('Próxima fecha de mantenimiento')
    