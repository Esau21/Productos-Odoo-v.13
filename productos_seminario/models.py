from odoo import models,fields

class Productos(models.Model):
    _name = "wb.productos"

    name = fields.Char("Nombre")
    descripcion = fields.Char("Descripcion")
    precio = fields.Integer("Precio")
    status = fields.Selection(selection=[("activo","Activo"),("desactivo","Desactivo")])