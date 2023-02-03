# -*- coding: utf-8 -*-

{
    'name': 'DIMAC21 Space Mission',
    'summary': 'An app to manage space missions',
    'description': 'To the moon and back!',
    'version': '1.0',
    'category': 'DIMAC21',
    'website': 'https://www.dimac21.com',
    'author': 'Soluciones DIMAC 21 C.A.',
    'license': 'LGPL-3',
    'depends': ['mail'],
    'data': [        
        # security
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        # views
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
    ],
    'demo': [
        'demo/space_mission_demo.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}