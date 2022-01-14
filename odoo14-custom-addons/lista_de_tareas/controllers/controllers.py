# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo02-scafold(http.Controller):
#     @http.route('/ejemplo02-scafold/ejemplo02-scafold/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo02-scafold/ejemplo02-scafold/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo02-scafold.listing', {
#             'root': '/ejemplo02-scafold/ejemplo02-scafold',
#             'objects': http.request.env['ejemplo02-scafold.ejemplo02-scafold'].search([]),
#         })

#     @http.route('/ejemplo02-scafold/ejemplo02-scafold/objects/<model("ejemplo02-scafold.ejemplo02-scafold"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo02-scafold.object', {
#             'object': obj
#         })
