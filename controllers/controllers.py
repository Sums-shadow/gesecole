# -*- coding: utf-8 -*-
# from odoo import http


# class Gesecoles(http.Controller):
#     @http.route('/gesecoles/gesecoles/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gesecoles/gesecoles/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gesecoles.listing', {
#             'root': '/gesecoles/gesecoles',
#             'objects': http.request.env['gesecoles.gesecoles'].search([]),
#         })

#     @http.route('/gesecoles/gesecoles/objects/<model("gesecoles.gesecoles"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gesecoles.object', {
#             'object': obj
#         })
