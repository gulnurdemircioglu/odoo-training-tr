from odoo import models, fields, api



class HrEmployee(models.Model):

    _inherit = 'hr.employee'  # database name


    identification_ids = fields.One2many(comodel_name='assignment.tool', inverse_name='user_name')
