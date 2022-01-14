# -*- coding: utf-8 -*-
from odoo import models, fields, api
class lista_de_tareas(models.Model):
    _name = 'lista_de_tareas.lista_de_tareas'
    _description = 'lista_de_tareas.lista_de_tareas'
#   Elementos de cada fila del modelo de datos
#   Los tipos de datos a usar en el ORM son
#   https://www.odoo-com/documentation/14.0/developer/reference/addons/orm.html
#   fields
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    fechaFin = fields.Date()
    realizada = fields.Boolean()

    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_urgente(self):
    
    
    #Para cada registro
        for record in self:
        #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
   