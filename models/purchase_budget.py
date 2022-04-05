# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import ValidationError


class PurchaseBudgetDetail(models.Model):
    _name = 'purchase_budget.detail'

    budget_post_id = fields.Many2one('account.budget.post', string="Budget post")
    product_id = fields.Many2one('product.product','Producto')
    valor = fields.Float('Valor presupuestado')
