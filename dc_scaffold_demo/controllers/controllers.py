# -*- coding: utf-8 -*-
# from odoo import http


# class DcScaffoldDemo(http.Controller):
#     @http.route('/dc_scaffold_demo/dc_scaffold_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dc_scaffold_demo/dc_scaffold_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dc_scaffold_demo.listing', {
#             'root': '/dc_scaffold_demo/dc_scaffold_demo',
#             'objects': http.request.env['dc_scaffold_demo.dc_scaffold_demo'].search([]),
#         })

#     @http.route('/dc_scaffold_demo/dc_scaffold_demo/objects/<model("dc_scaffold_demo.dc_scaffold_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dc_scaffold_demo.object', {
#             'object': obj
#         })
