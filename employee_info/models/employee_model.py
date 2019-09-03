from odoo import api, fields, models
from odoo.odoo.exceptions import ValidationError
from datetime import timedelta


class Employee_Info(models.Model):
    _name = 'employee.info'
    _description = "Employee Info"

    # employees_name = fields.Char('Employee Names')
    employees_name = fields.Many2one('hr.employee', string="Personel Adı", required=True)
    types = fields.Selection([
        ('passport', 'Passport'),
        ('id_card', 'ID Card'),
        ('driving_license', 'Driving License')
    ], string='Card Type')
    identification_number = fields.Integer(string = 'Identification Number')
