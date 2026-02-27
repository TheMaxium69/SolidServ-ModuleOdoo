from odoo import models, fields

class TypeServer(models.Model):
    _name = 'solidserv.server.type'
    _description = 'Type de Serveur'

    name = fields.Char('Nom du type', required=True)
    display_name = fields.Char('Nom d\'affichage')
    color = fields.Integer('Couleur')

class StatusServer(models.Model):
    _name = 'solidserv.server.status'
    _description = 'Statut de Serveur'

    name = fields.Char('Nom de Statut', required=True)
    color = fields.Integer('Couleur')

class RecurrenceServer(models.Model):
    _name = 'solidserv.server.recurrence'
    _description = 'Récurrence d\'abonnement de Serveur'

    name = fields.Char('Nom de la Récurrence', required=True)

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

    # Global
    currency_id = fields.Many2one(
        'res.currency',
        string='Devise',
        default=lambda self: self.env.company.currency_id
    )

    # Identite
    name = fields.Char('Nom', required=True)
    alias = fields.Char('Alias')
    type_id = fields.Many2one('solidserv.server.type', string='Type')
    type_color = fields.Integer(related='type_id.color', store=True)
    date_create = fields.Date('Mise en service')

    # Serveur
    status_id = fields.Many2one('solidserv.server.status', string='Statut')
    status_color = fields.Integer(related='status_id.color', store=True)
    ip_public = fields.Char('IP Publique')
    ip_private = fields.Char('IP Privé')
    proxy_id = fields.Many2one('solidserv.server', string='Proxy')

    # Technique
    os_id = fields.Many2one('solidserv.server.os', string='OS')
    os_version = fields.Char(related='os_id.version', store=True)
    os_type = fields.Char(related='os_id.os_type', store=True)
    cpu = fields.Char('Processeur')
    ram = fields.Char('Ram')
    rom = fields.Char('Stockage')
    tyro_uptime_state = fields.Boolean('État du TyroUptime')
    id_vm = fields.Char('Id VM')

    # Hebergeur
    hebergeur_id = fields.Many2one('res.partner', string='Hébergeur')
    baremetal_id = fields.Many2one('solidserv.server', string='Bare Métal')
    location_id = fields.Many2one('solidserv.server.location', string='Lieu')
    location_country = fields.Char(related='location_id.country', store=True)
    price_purchase = fields.Monetary('Prix d\'achat', currency_field='currency_id')
    date_purchase = fields.Date('Date d\'achat')
    recurrence_purchase = fields.Many2one('solidserv.server.recurrence', string='Récurrence d\'achat')

    # Client
    client_ids = fields.Many2many('res.partner', string='Clients')
    price_sale = fields.Monetary('Prix de vente', currency_field='currency_id')
    date_sale  = fields.Date('Date de vente')
    recurrence_sale = fields.Many2one('solidserv.server.recurrence', string='Récurrence de vente')

    # SIDE
    content = fields.Text('Description')
    notes = fields.Html('Notes Internes')