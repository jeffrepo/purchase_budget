# -*- coding: utf-8 -*-
{
    'name': "Purchase Budget",

    'summary': """Purchase BUdget """,

    'description': """
        Módulo para verificar las compras y no pasar del presupuesto
    """,

    'author': "Stechnologies",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['account_budget','purchase'],

    'data': [
        'views/account_budget_views.xml',
    ],
    'qweb': [
    ],
}
