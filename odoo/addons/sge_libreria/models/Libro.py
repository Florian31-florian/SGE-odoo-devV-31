
from odoo import models, fields, api

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'
    
    name = fields.Char('Título',required=True)
    precio = fields.Float('Precio',required=True)
    ejemplares = fields.Integer('Ejemplares')
    fecha_compra = fields.Date('Fecha de compra')
    segmano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1','Regular'),
        ('2','Malo')
    ], string='Estado',default='0')