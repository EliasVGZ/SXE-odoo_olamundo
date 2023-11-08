# -*- coding: utf-8 -*-
# from odoo import http


# class /home/a22eliassvf/pycharmProjects/odooOlamundo(http.Controller):
#     @http.route('//home/a22eliassvf/pycharm_projects/odoo_olamundo//home/a22eliassvf/pycharm_projects/odoo_olamundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/a22eliassvf/pycharm_projects/odoo_olamundo//home/a22eliassvf/pycharm_projects/odoo_olamundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/a22eliassvf/pycharm_projects/odoo_olamundo.listing', {
#             'root': '//home/a22eliassvf/pycharm_projects/odoo_olamundo//home/a22eliassvf/pycharm_projects/odoo_olamundo',
#             'objects': http.request.env['/home/a22eliassvf/pycharm_projects/odoo_olamundo./home/a22eliassvf/pycharm_projects/odoo_olamundo'].search([]),
#         })

#     @http.route('//home/a22eliassvf/pycharm_projects/odoo_olamundo//home/a22eliassvf/pycharm_projects/odoo_olamundo/objects/<model("/home/a22eliassvf/pycharm_projects/odoo_olamundo./home/a22eliassvf/pycharm_projects/odoo_olamundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/a22eliassvf/pycharm_projects/odoo_olamundo.object', {
#             'object': obj
#         })
