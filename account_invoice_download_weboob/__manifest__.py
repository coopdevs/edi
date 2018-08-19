# -*- coding: utf-8 -*-
# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Download Weboob',
    'version': '10.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Auto-download supplier invoices with Weboob',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': [
        'account_invoice_download',
        ],
    'external_dependencies': {'python': ['weboob']},
    'data': [
        'views/account_invoice_download_config.xml',
        'views/weboob_module.xml',
        'wizard/weboob_module_update_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
