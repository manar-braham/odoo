from odoo import models, fields, api


class GymPaiement(models.Model):
    #_inherit='account.payment'
    _name = 'gym.paiement'
    _description = 'Gym Paiement'

    client_id = fields.Many2one('gym.client', string='Client', required=True)
    date = fields.Date(string='Date du paiement', required=True)
    amount = fields.Float(string='Montant', required=True)
    payment_method = fields.Selection([
        ('cash', 'Espèces'),
        ('card', 'Carte bancaire'),
        ('online', 'Paiement en ligne')
    ], string='Mode de paiement', required=True)