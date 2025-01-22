from odoo import models, fields, api


class GymSession(models.Model):
    _name = 'gym.session'
    _description = 'Gym Session'

    name = fields.Char(string='Nom de la session', required=True)
    date = fields.Datetime(string='Date et heure', required=True)
    duration = fields.Float(string='Durée (heures)', required=True)
    trainer_id = fields.Many2one('gym.trainer', string='Entraineur', required=True)
    client_ids = fields.Many2many('gym.client', string='Clients')