# -*- coding: utf-8 -*-

{
    'name': 'Academia DIMAC21',
    'summary': 'Módulo de academia para Odoo',
    'description': 'Módulo de academia para Odoo v16 ofrecido por Soluciones DIMAC21.',
    'version': '1.0',
    'category': 'DIMAC21',
    'website': 'https://www.dimac21.com',
    'author': 'Soluciones DIMAC21',
    'license': 'LGPL-3',
    'depends': ['base'],
    'views': [        
        # security
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/academy_demo.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}