```python
from odoo import http
from odoo.http import request

class PaymentMethodController(http.Controller):

    @http.route('/payment_method/data', type='json', auth='user')
    def get_payment_method_data(self, **kwargs):
        payment_method_model = request.env['payment.method']
        payment_methods = payment_method_model.search([])
        return {
            'payment_methods': [method.read()[0] for method in payment_methods]
        }

    @http.route('/payment_method/update', type='json', auth='user')
    def update_payment_method(self, payment_method_id, **kwargs):
        payment_method_model = request.env['payment.method']
        payment_method = payment_method_model.browse(payment_method_id)
        if 'name' in kwargs:
            payment_method.name = kwargs['name']
        if 'description' in kwargs:
            payment_method.description = kwargs['description']
        payment_method.save()
        return {'status': 'success'}

    @http.route('/payment_method/delete', type='json', auth='user')
    def delete_payment_method(self, payment_method_id):
        payment_method_model = request.env['payment.method']
        payment_method = payment_method_model.browse(payment_method_id)
        payment_method.unlink()
        return {'status': 'success'}
```