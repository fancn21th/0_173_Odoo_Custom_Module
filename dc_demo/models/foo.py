# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Foo(models.Model):
    _name = "dc.foo"
    _description = "foo"

    name = fields.Char(string="Name", required=True, translate=True)

    start_datetime = fields.Datetime('Start DateTime', default=fields.Datetime.now())

    state = fields.Selection([
        ('bar', 'bar'),
        ('baz', 'baz'),
    ], required=True, default="bar")