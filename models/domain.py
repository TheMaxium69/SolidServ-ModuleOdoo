from odoo import models, fields

class Domain(models.Model):
    _name = 'solidserv.domain'
    _description = 'Nom de domaine'

    # Global
    currency_id = fields.Many2one(
        'res.currency',
        string='Devise',
        default=lambda self: self.env.company.currency_id
    )

    # Identite
    name = fields.Char('Nom du domaine', required=True)
    type = fields.Char('Type de domaine')
    date_create = fields.Date('Mise en service')
    main_id = fields.Many2one('solidserv.domain', string='Domaine Principal')

    def action_open_domain(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://' + self.name,
            'target': 'new',
        }

    # Hebergeur
    hebergeur_id = fields.Many2one('res.partner', string='Hébergeur')
    price_purchase = fields.Monetary('Prix d\'achat', currency_field='currency_id')
    date_purchase = fields.Date('Date d\'achat')
    recurrence_purchase = fields.Many2one('solidserv.server.recurrence', string='Récurrence d\'achat')

    # Client
    client_ids = fields.Many2many('res.partner', string='Clients')
    price_sale = fields.Monetary('Prix de vente', currency_field='currency_id')
    date_sale = fields.Date('Date de vente')
    recurrence_sale = fields.Many2one('solidserv.server.recurrence', string='Récurrence de vente')

    # SIDE
    content = fields.Text('Description')
    notes = fields.Html('Notes Internes')