# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanMemalak(http.Controller):
#     @http.route('/latihan_memalak/latihan_memalak/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_memalak/latihan_memalak/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_memalak.listing', {
#             'root': '/latihan_memalak/latihan_memalak',
#             'objects': http.request.env['latihan_memalak.latihan_memalak'].search([]),
#         })

#     @http.route('/latihan_memalak/latihan_memalak/objects/<model("latihan_memalak.latihan_memalak"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_memalak.object', {
#             'object': obj
#         })
