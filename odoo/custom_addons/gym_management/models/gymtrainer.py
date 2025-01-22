from odoo import models, fields, api


class GymTrainer(models.Model):
    _name = 'gym.trainer'
    _description = 'Gym Trainer'

    name = fields.Char(string="Nom de l'entraineur", required=True)
    speciality = fields.Char(string='Spécialité')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Téléphone')
    active = fields.Boolean(string='Actif', default=True)