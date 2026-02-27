from odoo import models, fields

class TypeServer(models.Model):
    _name = 'solidserv.server.type'
    _description = 'Type de Serveur'

    name = fields.Char('Nom du type', required=True)
    display_name = fields.Char('Nom d\'affichage')
    color = fields.Integer('Couleur')

class LocationServer(models.Model):
    _name = 'solidserv.server.location'
    _description = 'Lieu des DataCenters'

    name = fields.Char('Nom du lieu', required=True)
    country = fields.Char('Pays')

class OsServer(models.Model):
    _name = 'solidserv.server.os'
    _description = 'OS de Serveur'

    name = fields.Char('Nom de l\'OS', required=True)
    version = fields.Char('Version de l\'OS')
    os_type = fields.Char('Type de l\'OS')

class Server(models.Model):
    _name = 'solidserv.server'
    _description = 'Serveur SolidServ'

    # Identite
    name = fields.Char('Nom', required=True)
    alias = fields.Char('Alias')
    type_id = fields.Many2one('solidserv.server.type', string='Type')
    type_color = fields.Integer(related='type_id.color', store=True)

    # Serveur
    ip_public = fields.Char('IP Publique')
    ip_private = fields.Char('IP Privé')
    location_id = fields.Many2one('solidserv.server.location', string='Lieu')
    location_country = fields.Char(related='location_id.country', store=True)

    # Technique
    os_id = fields.Many2one('solidserv.server.os', string='OS')
    os_version = fields.Char(related='os_id.version', store=True)
    os_type = fields.Char(related='os_id.os_type', store=True)
    cpu = fields.Char('Processeur')
    ram = fields.Char('Ram')
    rom = fields.Char('Stockage')

    # SIDE
    content = fields.Text('Description')
    notes = fields.Html('Notes Internes')