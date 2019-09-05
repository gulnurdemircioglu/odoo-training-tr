from odoo import models, fields,api



class AssignmentTool(models.Model):

    _name = 'assignment.tool'  # database name
    _description = 'It assignment tool'

    @api.model
    def get_current_employee(self):
        current_employee = self.env.user.employee_ids
        if current_employee:
            return current_employee[-1].id
        return False

    obj_id = fields.Char()
    user_name= fields.Many2one('res.users', 'Employee', default=lambda self: self.env.user.id, readonly=True)
    # user_id = fields.Char('User ID', related='user_name.uid', readonly=True)
    obj_type=fields.Selection([
        ('computer',"Computer"),
        ('screen', "Screen"),
        ('keyboard_mouse', "Keyboard and Mouse"),
        ('network_computer', "Network Computer"),
        ('telephone', "Telephone"),
        ('printer', "Printer")

    ])
    date = fields.Date(string='Validation Date')
    assignment_status = fields.Selection([
        ('valid', "Valid"),
        ('invalid', "Invalid")
    ], default='invalid' ,string='Assignment Status' )

    description = fields.Text(string='Assignment Details')


