{
    'name': 'Control Expiration Date',
    'version': '9.0.0',
    'description': 'Coloca un campo llamado "Dias de fecha de expiracion" en company-->settings que declara el numero de dias del expiration date de sale order',
    'author': 'Raul Ovalle, raulovallet@gmail.com',
    'depends': ['sale'],
    'data': ['views/res_company_view.xml',
             'views/sale_order_view.xml'
             ],
    'installable': True,
}