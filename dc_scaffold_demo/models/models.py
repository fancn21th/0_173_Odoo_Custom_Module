# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dc_scaffold_demo(models.Model):
#     _name = 'dc_scaffold_demo.dc_scaffold_demo'
#     _description = 'dc_scaffold_demo.dc_scaffold_demo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
