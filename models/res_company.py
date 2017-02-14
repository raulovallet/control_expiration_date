from openerp import models, fields, api

class ControlExpirationDateResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    days_validity_date = fields.Integer('Dias de fecha de expiracion')
