# -*- coding: utf-8 -*-

{
    'name': 'Misión Espacial DIMAC21',
    'summary': 'Misión Espacial de DIMAC21',
    'description': 'Hasta la luna y de regreso.',
    'version': '1.0',
    'category': 'DIMAC21',
    'website': 'https://www.dimac21.com',
    'author': 'Soluciones DIMAC21',
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