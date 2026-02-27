{
    'name': "SolidServ",

    'summary': "Module pour le projet SolidServ",

    'description': """
SolidServ est un module Odoo propriétaire conçu spécifiquement pour la gestion, le monitoring et l'automatisation des infrastructures serveurs au sein de la filiale SolidServ. Ce module centralise le contrôle des ressources machines pour les besoins exclusifs de Tyrolium, offrant une interface unifiée entre la gestion administrative d'Odoo et les impératifs techniques du terrain.
    """,

    'author': "Tyrolium",
    'website': "https://tyrolium.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

