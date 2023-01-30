# -*- coding: utf-8 -*-

{
    'name': 'Biblioteca DIMAC21',
    'summary': 'Módulo de biblitoeca para Odoo v16 ofrecido por Soluciones DIMAC21.',
    'description': 'Toda una gama de funcionalidades para la gestión de una biblioteca.',
    'version': '1.0',
    'category': 'DIMAC21',
    'website': 'https://www.dimac21.com',
    'author': 'Soluciones DIMAC21',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [        
        # security
        'security/library_security.xml',
        'security/ir.model.access.csv',
        # views
        'views/library_menuitems.xml',
        'views/book_views.xml',
    ],
    'demo': [
        'demo/library_demo.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}