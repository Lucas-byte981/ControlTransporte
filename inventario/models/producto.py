# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Modelo de los productos

class Producto(models.Model):
    _name = 'inventario.producto'

    name = fields.Char(string="Nombre", required=True)
    date_elaboration = fields.Date(string = "Fecha de elaboración")
    date_expiration = fields.Date(string = "Fecha de vencimiento")
    categorias_id = fields.Many2one('inventario.categoria_producto', string="Categoría")
   
class CategoriaProducto(models.Model):
    _name = 'inventario.categoria_producto'
    name = fields.Char(string="Nombre", required=True)
    producto_ids = fields.One2many(
        'inventario.producto',
        'categorias_id',
        string = 'Productos')

    total_productos = fields.Integer(string = "Total Productos", compute =  "_total_productos")

    
    @api.one
    def _total_productos(self):
        self.total_productos = len(self.producto_ids)