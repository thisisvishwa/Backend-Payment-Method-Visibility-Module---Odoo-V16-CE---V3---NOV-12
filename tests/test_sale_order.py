```python
from odoo.tests import common

class TestSaleOrder(common.TransactionCase):

    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.sale_order = self.env['sale.order']
        self.payment_method = self.env['payment.method']

    def test_sale_order_creation(self):
        # Test case for sale order creation
        order = self.sale_order.create({
            'name': 'Test Order',
            'partner_id': 1,
        })
        self.assertEqual(order.name, 'Test Order')

    def test_payment_method_visibility(self):
        # Test case for payment method visibility in sale order
        order = self.sale_order.create({
            'name': 'Test Order',
            'partner_id': 1,
            'payment_method_id': 1,
        })
        self.assertEqual(order.payment_method_id.id, 1)

    def test_sale_order_filter(self):
        # Test case for sale order filter by payment method
        order1 = self.sale_order.create({
            'name': 'Test Order 1',
            'partner_id': 1,
            'payment_method_id': 1,
        })
        order2 = self.sale_order.create({
            'name': 'Test Order 2',
            'partner_id': 1,
            'payment_method_id': 2,
        })
        orders = self.sale_order.search([('payment_method_id', '=', 1)])
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].id, order1.id)

    def test_sale_order_sorting(self):
        # Test case for sale order sorting by payment method
        order1 = self.sale_order.create({
            'name': 'Test Order 1',
            'partner_id': 1,
            'payment_method_id': 1,
        })
        order2 = self.sale_order.create({
            'name': 'Test Order 2',
            'partner_id': 1,
            'payment_method_id': 2,
        })
        orders = self.sale_order.search([], order='payment_method_id')
        self.assertEqual(orders[0].id, order1.id)
        self.assertEqual(orders[1].id, order2.id)
```