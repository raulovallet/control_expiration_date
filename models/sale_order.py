from openerp import models, fields, api
from datetime import datetime, timedelta

class ControlExpirationDateSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):

        if vals.get('date_order'):
            vals.update({'validity_date':datetime.strptime(vals.get('date_order'), '%Y-%m-%d %H:%M:%S') + timedelta(days=self.env.user.company_id.days_validity_date)})
        else:
            vals.update({'validity_date':datetime.now() + timedelta(days=self.env.user.company_id.days_validity_date)})
        return super(ControlExpirationDateSaleOrder, self).create(vals)

