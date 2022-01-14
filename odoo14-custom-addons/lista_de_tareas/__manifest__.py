# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",
    'summary': """
        Sencilla lista de tareas""",
    'description': """
        Sencilla lista de tareas para desarrollar una organizacion ordenada.
    """,
    'author': "Alejandro Martín",
    'website': "https://github.com/Akame545",
    'application': "True",
    'category': 'Productivity',
    'version': '0.1',
#   Módulos necesarios para que este funcione
    'depends': ['base'],
    'data': [
        #indica la política de acceso al módulo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
