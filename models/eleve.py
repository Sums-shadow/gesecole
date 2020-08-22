# -*- coding: utf-8 -*-

from odoo import models, fields, api



class eleve(models.Model):
    _inherit='hr.employee'

    parents_id=fields.Many2one('gesecoles.parent')
    classe_id=fields.Many2one('gesecoles.classe')
    section_id=fields.Many2one('gesecoles.section')



class parent(models.Model):
    _name='gesecoles.parent'
    _rec_name='nom'

    nom=fields.Char('nom du parent')
    telephone=fields.Char('telephone')


class classe(models.Model):
    _name='gesecoles.classe'
    _rec_name='titre'

    titre=fields.Char('titre de la classe')


class classe(models.Model):
    _name='gesecoles.section'
    _rec_name='titre'

    titre=fields.Char('titre de la section')