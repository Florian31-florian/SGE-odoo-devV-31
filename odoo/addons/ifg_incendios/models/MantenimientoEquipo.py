from odoo import models, fields, api



class MantenimientoEquipo(models.Model):
  _name = 'ifg_incendios.mantenimiento'
  _description = 'ifg_incendios.Mantenimiento Equipo'

  equipo_id = fields.Many2one('ifg_incendios.equipo', string='Equipo', required=True)
  fecha_mantenimiento = fields.Date(string='Fecha de mantenimiento', required=True)
  tipo_mantenimiento = fields.Selection([
      ('preventivo', 'Preventivo'),
      ('correctivo', 'Correctivo')
  ], string='Tipo de mantenimiento', required=True)
  descripcion = fields.Text(string='Descripción del mantenimiento')
  coste = fields.Float(string='Coste del mantenimiento')    
    
