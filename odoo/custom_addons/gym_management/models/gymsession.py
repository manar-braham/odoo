from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import logging

# Créez un logger pour suivre les événements
_logger = logging.getLogger(__name__)


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

    # Champ pour sélectionner un client spécifique
    selected_client = fields.Many2one('gym.client', string="Client sélectionné", domain="[('is_active', '=', True)]")

    @api.depends('client_ids')
    def _compute_current_participants(self):
        for session in self:
            session.current_participants = len(session.client_ids)

    @api.constrains('client_ids')
    def _check_max_participants(self):
        for session in self:
            if len(session.client_ids) > session.max_participants:
                raise ValidationError(
                    f"Le nombre de participants pour la session '{session.name}' dépasse le maximum de {session.max_participants}.")

    def send_confirmation_email(self, client):
        """Envoie un e-mail de confirmation à un client."""
        if not client.email:
            raise UserError(f"Le client {client.name} n'a pas d'adresse email.")

        _logger.info(f"Envoi de l'email de confirmation à {client.name} pour la session {self.name}")

        subject = f"Confirmation de votre inscription à la session {self.name}"
        body = f"Bonjour {client.name},\n\nVous êtes inscrit à la session de gym '{self.name}' qui se tiendra le {self.date} pour une durée de {self.duration} heures.\n\nMerci pour votre inscription !"

        # Envoi de l'email
        mail_values = {
            'subject': subject,
            'body_html': body,
            'email_to': client.email,
        }

        # Créez et envoyez l'email
        try:
            mail = self.env['mail.mail'].create(mail_values)
            mail.send()
            _logger.info(f"Email envoyé avec succès à {client.email}")
        except Exception as e:
            _logger.error(f"Erreur lors de l'envoi de l'email : {e}")
            raise UserError(f"Erreur lors de l'envoi de l'email à {client.name}")

    def add_client_to_session(self):
        """Ajoute un client à la session et envoie un e-mail de confirmation."""
        # Vérification de la disponibilité
        if len(self.client_ids) >= self.max_participants:
            raise UserError(f"La session '{self.name}' est déjà complète.")

        # Récupère le client sélectionné
        client = self.selected_client
        if not client:
            raise UserError("Veuillez sélectionner un client.")

        # Ajout du client à la session
        self.client_ids = [(4, client.id)]

        # Envoi de l'email de confirmation
        self.send_confirmation_email(client)

    def check_availability(self):
        """Vérifie la disponibilité de places dans la session."""
        for session in self:
            available_slots = session.max_participants - session.current_participants
            if available_slots > 0:
                # Affiche une notification si des places sont disponibles
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
