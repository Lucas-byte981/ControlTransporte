# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Modelo de la clase de control

class Control(models.Model):
     _name = 'seguimiento.control'

     cliente= fields.Char(string="Cliente", required=True)
     area= fields.Char(string="Area de transporte", required=True)
     fecha= fields.Date(string="Fecha de transporte")
     temp_max= fields.Float(String="Temperatura máxima")
     temp_min= fields.Float(String="Temperatura mínima")
     hum_max= fields.Float(String="Humedad máxima")
     hum_min= fields.Float(String="Humedad mínima")

     detalle_control_ids= fields.One2many(
         'seguimiento.detalle_control', 'control_id', string="Detalle del seguimiento")

class DetalleControl(models.Model):
     _name= 'seguimiento.detalle_control'

     producto_id= fields.Many2one('inventario.producto', String="Producto")
     cantidad = fields.Integer(default=1)
     control_id= fields.Many2one('seguimiento.control', String="Control")