from odoo import models, fields

class Server(models.Model):
    _name = 'solidserv.server'
    _description = 'Serveur SolidServ'

    name = fields.Char('Nom', required=True)