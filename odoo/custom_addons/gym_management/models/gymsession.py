from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class GymSession(models.Model):
    _name = 'gym.session'
    _description = 'Gym Session'

    name = fields.Char(string='Nom de la session', required=True)
    date = fields.Datetime(string='Date et heure', required=True)
    duration = fields.Float(string='Durée (heures)', required=True)
    trainer_id = fields.Many2one('gym.trainer', string='Entraineur', required=True)
    client_ids = fields.Many2many('gym.client', string='Clients')
    # Nouveau champ pour la limite du nombre de participants
    max_participants = fields.Integer(string='Nombre maximum de participants', required=True, default=10)

    # Calcul du nombre actuel de participants
    current_participants = fields.Integer(string='Participants actuels', compute='_compute_current_participants',
                                          store=True)

    @api.depends('client_ids')
    def _compute_current_participants(self):
        for session in self:
            session.current_participants = len(session.client_ids)

    @api.constrains('client_ids')
    def _check_max_participants(self):
        for session in self:
            if len(session.client_ids) > session.max_participants:
                raise ValidationError(
                    f"Le nombre de participants pour la session '{session.name}' dépasse le maximum de {session.max_participants}."
                )

    def check_availability(self):
        for session in self:
            available_slots = session.max_participants - session.current_participants
            if available_slots > 0:
                # Afficher un message d'information
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Vérification de la disponibilité',
                        'message': f'Il reste {available_slots} place(s) pour la session "{session.name}".',
                        'type': 'success',  # Type de notification (success, warning, danger, etc.)
                        'sticky': False  # Cette notification disparaît après quelques secondes
                    }
                }
            else:
                raise UserError(f'Aucune place disponible pour la session "{session.name}".')