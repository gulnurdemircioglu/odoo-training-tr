from odoo import api, fields, models


class CertificationStandard(models.Model):
    _name = 'certification.standard'
    _description = "Certification Standard"

    name = fields.Char()
    description = fields.Text()
