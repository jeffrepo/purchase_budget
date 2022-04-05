# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountBudgetPost(models.Model):
    _inherit = "account.budget.post"

    detail_ids = fields.One2many('purchase_budget.detail','budget_post_id',string="Detalle")
