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
    'depends': ['sale_management', 'website'],
    'data': [        
        # security
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        # views
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        # inherited views
        'views/sales_view_inherit.xml',
        'views/product_views_inherit.xml',
        # wizards
        'wizard/sale_wizard_view.xml',
        # reports
        'reports/session_report_template.xml',
        # web templates
        'views/academy_web_templates.xml',
    ],
    'demo': [
        'demo/academy_demo.xml'
    ],
    'assets': {},
    'application': True,
    'installable': True,
    'auto_install': False,
}