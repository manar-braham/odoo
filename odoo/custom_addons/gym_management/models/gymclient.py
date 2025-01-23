from odoo import api, models, fields

class GymClient(models.Model):
    _name = 'gym.client'
    _description = 'Gym Client'

    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()  # Ensure this field exists
    is_active = fields.Boolean('Is Active', default=True)
    membership_type = fields.Selection([
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ], default='basic')
    has_subscription = fields.Boolean(string="Has Subscription", default=False)
    session_type = fields.Selection([
        ('aerobic', 'Aerobic'),
        ('yoga', 'Yoga'),
        ('zumba', 'Zumba'),
        ('weight_training', 'Weight Training'),
        ('cardio', 'Cardio'),
    ], string="Session Type")
    subscription_duration = fields.Integer(string="Subscription Duration (months)",
                                           help="Duration of the subscription in months")
    subscription_price = fields.Float(string="Subscription Price", help="Price of the subscription")

    @api.onchange('has_subscription')
    def _onchange_has_subscription(self):
        """Clear duration and price if the client is not subscribed."""
        if not self.has_subscription:
            self.subscription_duration = 0
            self.subscription_price = 0.0