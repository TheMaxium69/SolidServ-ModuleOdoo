# from odoo import http


# class Solidserv(http.Controller):
#     @http.route('/solidserv/solidserv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/solidserv/solidserv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('solidserv.listing', {
#             'root': '/solidserv/solidserv',
#             'objects': http.request.env['solidserv.solidserv'].search([]),
#         })

#     @http.route('/solidserv/solidserv/objects/<model("solidserv.solidserv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('solidserv.object', {
#             'object': obj
#         })

