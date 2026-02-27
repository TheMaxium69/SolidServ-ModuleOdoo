from odoo import models, fields

class Server(models.Model):
    _name = 'solidserv.server'
    _description = 'Serveur SolidServ'

    name = fields.Char('Nom', required=True)

    ipPublic = fields.Char('IP Publique')
    ipPrivate = fields.Char('IP Privé')

    cpu = fields.Char('Processeur')
    ram = fields.Char('Ram')
    rom = fields.Char('Stockage')

    content = fields.Text('Description')
    notes = fields.Html('Notes Internes')