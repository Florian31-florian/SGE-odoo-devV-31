# -*- coding: utf-8 -*-
# from odoo import http


# class IfgIncendios(http.Controller):
#     @http.route('/ifg_incendios/ifg_incendios', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ifg_incendios/ifg_incendios/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ifg_incendios.listing', {
#             'root': '/ifg_incendios/ifg_incendios',
#             'objects': http.request.env['ifg_incendios.ifg_incendios'].search([]),
#         })

#     @http.route('/ifg_incendios/ifg_incendios/objects/<model("ifg_incendios.ifg_incendios"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ifg_incendios.object', {
#             'object': obj
#         })

