# -*- coding:utf-8 -*-

from odoo import models, fields, api


class frais(models.Model):
    _inherit='hr.expense'

    eleve_id=fields.Many2one('hr.employee')
    classe=fields.Char(string="classe")
    parent=fields.Char(string="parent")


