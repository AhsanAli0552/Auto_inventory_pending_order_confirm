from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def sale_cron_invoices(self):
        orders = self.search([
            ('state', '=', 'sale'),
            ('invoice_ids', '=', False),
            ('partner_id.country_id.code', '=', 'US'),
            ('delivery_status','=','full')
        ])

        for order in orders:
            invoices = order._create_invoices()
            if invoices:
                invoices.action_post()
        return True