# -*- coding: utf-8 -*-

from odoo import models, fields, api


class milkway(models.Model):
    _name = 'milkway.milkway'
    _description = 'milkway.milkway'
    _rec_name = 'display_name'

    color = fields.Integer()
    display_name = fields.Char(string='Name', required=True)
    email = fields.Char('Email', required=True)
    mobile = fields.Char('Mobile', required=True)
    # avatar = fields.Image('Imagen tareas',max_width=50,max_heigth=50)
    # tarea = fields.Char()
    # prioridad = fields.Integer()
    # urgente = fields.Boolean(compute="_value_urgente", store=True)
    # fecha = fields.Date()
    # realizada = fields.Boolean()

    # #Este computo depende de la variable prioridad
    # @api.depends('prioridad')
    # #Funcion para calcular el valor de urgente
    # def _value_urgente(self):
    # #Para cada registro
    #     for record in self:
    #     #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
    #         if record.prioridad>10:
    #             record.urgente = True
    #         else:
    #             record.urgente = False
