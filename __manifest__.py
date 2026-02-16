# -*- coding: utf-8 -*-
{
    'name': "sale_cron_update",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose
 """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale','accountant','stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_cron_invoice.xml',
    ],
}

