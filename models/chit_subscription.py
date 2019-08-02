# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules

class Subscription(models.Model):
    _name = 'chit.subscription'

    _description = 'Subscriber Details'

    # sub_name = fields.Char(string="Name")
    # sub_contact = fields.Char(string="Contact")
    g_id = fields.Char(string="Group Id")
    auction_date = fields.Datetime(string="Auction Date", required=False,)
    number_of_clients = fields.Integer(string="Number Of Clients")

    group_description = fields.Char(string="Group Description")
    subscription_date = fields.Datetime(string="Subscription Date", required=False,)
    installment_amount = fields.Float(string="Installment Amount")

    date = fields.Datetime(string="Date", required=False,)
    due_date = fields.Datetime(string="Due Date", required=False, )

    detail_id = fields.One2many('chit.subscription.detail', 'header_id', string="Subscriber")


class SubscriptionDetails(models.Model):
    _name = 'chit.subscription.detail'

    header_id = fields.Many2one('chitfund.chitfund', string="Subscriber")
    client_name = fields.Char(string="Client Name")
    subscription_date = fields.Datetime(string="Subscription Date", required=False, )
    installment_amount = fields.Float(string="Installment Amount")
    bank_name = fields.Char(string="Bank Name")
    bank_reference = fields.Char(string="Bank Reference")
    paid_amount = fields.Char(string="Paid amount")
    cumulative_instalement_amount = fields.Char(string="Cumulative Installment Amount")