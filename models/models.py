# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules


class chitfund(models.Model):
    _name = 'chitfund.chitfund'
    _description = 'Chitfund Details'
    # _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    # name = fields.Char("Subscriber Name")
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    chit_name = fields.Char(string="Chit Name", required=True)
    chit_code = fields.Char("Chit Code")
    chit_amount = fields.Float("Chit Amount")
    number_of_clients = fields.Integer("Number Of Clients")
    installment_amount = fields.Float("Installment Amount")
    auction_date = fields.Datetime(string="Auction Date", required=False,)
    subscription_date = fields.Datetime(string="Subscription Date", required=False,)
    due_date = fields.Datetime(string="Due Date", required=False,)
    description = fields.Text()

    # chit_id = fields.One2many('chit.clients', 'chitfund_id', string="Contacts")
    # chit_id = fields.One2many('chit.class', 'customer_id', string="Add Client")
    chit_id = fields.One2many('chit.class', 'user_id', string="Add Client")
    test_id = fields.Many2many('res.partner', 'chit_id')


class Chitclients(models.Model):
    _name = 'chit.class'

    user_id = fields.Many2one('res.partner', string="Clients", stored=True, readonly=False)
    ticket_no = fields.Char(string="Ticket No")











