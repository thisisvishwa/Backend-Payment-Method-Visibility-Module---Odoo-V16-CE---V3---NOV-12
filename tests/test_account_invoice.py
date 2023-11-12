```python
from odoo.tests import common

class TestAccountInvoice(common.TransactionCase):

    def setUp(self):
        super(TestAccountInvoice, self).setUp()
        self.AccountInvoice = self.env['account.invoice']
        self.SaleOrder = self.env['sale.order']
        self.PaymentMethod = self.env['payment.method']

    def test_create_invoice(self):
        # Create a new sale order
        sale_order = self.SaleOrder.create({
            'name': 'Test Order',
            # Add other necessary fields
        })

        # Create a new payment method
        payment_method = self.PaymentMethod.create({
            'name': 'Test Payment Method',
            # Add other necessary fields
        })

        # Create a new invoice
        invoice = self.AccountInvoice.create({
            'name': 'Test Invoice',
            'order_id': sale_order.id,
            'payment_method_id': payment_method.id,
            # Add other necessary fields
        })

        # Check if the invoice is created
        self.assertEqual(invoice.name, 'Test Invoice')

    def test_update_invoice(self):
        # Create a new invoice
        invoice = self.AccountInvoice.create({
            'name': 'Test Invoice',
            # Add other necessary fields
        })

        # Update the invoice
        invoice.write({
            'name': 'Updated Test Invoice',
        })

        # Check if the invoice is updated
        self.assertEqual(invoice.name, 'Updated Test Invoice')

    def test_delete_invoice(self):
        # Create a new invoice
        invoice = self.AccountInvoice.create({
            'name': 'Test Invoice',
            # Add other necessary fields
        })

        # Delete the invoice
        invoice.unlink()

        # Check if the invoice is deleted
        self.assertEqual(len(self.AccountInvoice.search([('name', '=', 'Test Invoice')])), 0)
```