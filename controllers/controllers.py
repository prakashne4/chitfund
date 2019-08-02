# -*- coding: utf-8 -*-
from odoo import http

class Chitfund(http.Controller):
    @http.route('/chitfund/chitfund/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/chitfund/chitfund/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('chitfund.listing', {
            'root': '/chitfund/chitfund',
            'objects': http.request.env['chitfund.chitfund'].search([]),
        })

    @http.route('/chitfund/chitfund/objects/<model("chitfund.chitfund"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('chitfund.object', {
            'object': obj
        })