from odoo import models, fields


class MoteurDatabase(models.Model):
    _name = 'solidserv.database.moteur'
    _description = 'Moteur de base de données'

    name = fields.Char('Nom du moteur', required=True)

class Database(models.Model):
    _name = 'solidserv.database'
    _description = 'Base de données'

    name = fields.Char('Nom', required=True)
    server_id = fields.Many2one('solidserv.server', string='Serveur')
    hebergeur_id = fields.Many2one(related='server_id.hebergeur_id', string='Hébergeur', store=True)
    location_id = fields.Many2one(related='server_id.location_id', string='Lieu', store=True)
    location_country = fields.Char(related='server_id.location_country', store=True)
    os_id = fields.Many2one(related='server_id.os_id', string='OS', store=True)
    status_id = fields.Many2one('solidserv.server.status', string='Statut')
    status_color = fields.Integer(related='status_id.color', store=True)
    database = fields.Char('Base de données')
    table = fields.Char('Table')
    client_ids = fields.Many2many(
        'res.partner',
        relation='solidserv_database_partner_rel',
        string='Clients'
    )
    moteur_id = fields.Many2one('solidserv.database.moteur', string='Moteur')

    # SIDE
    content = fields.Text('Description')
    notes = fields.Html('Notes Internes')