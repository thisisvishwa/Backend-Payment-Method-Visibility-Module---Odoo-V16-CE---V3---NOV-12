```python
from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')

    @api.multi
    def action_invoice_open(self):
        res = super(AccountInvoice, self).action_invoice_open()
        self.update_payment_method()
        return res

    @api.multi
    def update_payment_method(self):
        for invoice in self:
            sale_order = self.env['sale.order'].search([('name', '=', invoice.origin)], limit=1)
            if sale_order and sale_order.payment_method_id:
                invoice.payment_method_id = sale_order.payment_method_id.id

    @api.multi
    def action_invoice_cancel(self):
        res = super(AccountInvoice, self).action_invoice_cancel()
        self.update_payment_method()
        return res
```