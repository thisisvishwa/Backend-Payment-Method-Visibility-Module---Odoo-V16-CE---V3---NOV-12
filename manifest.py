{
    'name': 'payment_method_visibility',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Enhanced Backend Payment Method Visibility Module',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'description': """
    Enhanced Backend Payment Method Visibility Module
    =================================================
    This module provides detailed visibility and management of payment methods in various standard views.
    """,
    'depends': ['base', 'sale', 'account', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'security/res_groups.xml',
        'views/payment_method_views.xml',
        'views/sale_order_views.xml',
        'views/account_invoice_views.xml',
        'views/settings_views.xml',
        'data/ir_actions_server_data.xml',
        'data/mail_template_data.xml',
        'report/payment_method_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/module.xml'],
    'test': [
        'tests/test_payment_method.py',
        'tests/test_sale_order.py',
        'tests/test_account_invoice.py',
    ],
}
