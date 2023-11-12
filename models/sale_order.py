```python
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')

    @api.onchange('payment_method_id')
    def _onchange_payment_method(self):
        # Logic to handle changes in payment method

    @api.model
    def create(self, vals):
        # Logic to handle creation of a new sale order with a payment method
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        # Logic to handle updates to a sale order's payment method
        return super(SaleOrder, self).write(vals)

    def action_confirm(self):
        # Logic to handle confirmation of a sale order
        return super(SaleOrder, self).action_confirm()

    def action_cancel(self):
        # Logic to handle cancellation of a sale order
        return super(SaleOrder, self).action_cancel()

    def action_draft(self):
        # Logic to handle resetting a sale order to draft
        return super(SaleOrder, self).action_draft()

    def _get_report_base_filename(self):
        # Logic to handle generation of a report filename
        return super(SaleOrder, self)._get_report_base_filename()
```