# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "It Assignment",
    "summary": "Define assignments for employees",
    'version': '12.0.1.0.0',
    "category": "Certification  Management",
    "website": "https://github.com/klcftm",
    "author": "Server Error",
    "license": "AGPL-3",
    "depends": [
        'base','hr'
    ],
    "data": [
        'security/ir.model.access.csv',
        'view/user.xml',
        'view/assignment_tool_view.xml'

    ],

    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
    'installable': True,
    'application': True,
}
