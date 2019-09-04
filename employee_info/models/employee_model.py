from odoo import api, fields, models
from odoo.odoo.exceptions import ValidationError
from datetime import timedelta


class Employee_Info(models.Model):
    _name = 'employee.info'
    _description = "Employee Info"
    # _inherit = "hr.employee"

    # employees_name = fields.Char('Employee Names')
    @api.model
    def get_current_employee(self):
        current_employee = self.env.user.employee_ids
        if current_employee:
            return current_employee[-1].id
        return False
    employees_name = fields.Many2one('hr.employee', string="Personel Adı", required=True ,default=get_current_employee)

    work_phone = fields.Char('Telefon Numarası', related='employees_name.work_phone', readonly=True)

    types = fields.Selection([
        ('passport', 'Passport'),
        ('id_card', 'ID Card'),
        ('driving_license', 'Driving License')
    ], string='Card Type')
    identification_number = fields.Integer(string = 'Identification Number')
