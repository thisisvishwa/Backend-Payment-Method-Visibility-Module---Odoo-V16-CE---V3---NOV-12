```python
from odoo import models, fields, api

class PaymentMethod(models.Model):
    _name = 'payment.method'
    _description = 'Payment Method'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    payment_gateway_id = fields.Many2one('payment.gateway', string='Payment Gateway')

    @api.model
    def create(self, vals):
        record = super(PaymentMethod, self).create(vals)
        # Add your custom logic here
        return record

    def write(self, vals):
        result = super(PaymentMethod, self).write(vals)
        # Add your custom logic here
        return result

    def unlink(self):
        # Add your custom logic here
        return super(PaymentMethod, self).unlink()

    @api.model
    def get_payment_methods(self):
        # Add your custom logic here
        return []

    @api.model
    def get_payment_method(self, payment_method_id):
        # Add your custom logic here
        return self.browse(payment_method_id)
```