# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
import dateutil.parser

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    def button_confirm(self):
        res = super().button_confirm()
        for order in self:
            date_order = dateutil.parser.parse(str(order.date_order)).date()
            if order.order_line:
                for line in order.order_line:
                    if line.account_analytic_id and line.account_analytic_id.crossovered_budget_line:
                        for budget_line in line.account_analytic_id.crossovered_budget_line:
                            if budget_line.general_budget_id and budget_line.general_budget_id.detail_ids and date_order >= budget_line.date_from and date_order <= budget_line.date_to:
                                for detail_line in budget_line.general_budget_id.detail_ids:
                                    if line.product_id.id == detail_line.product_id.id:
                                        purchase_order_line_ids = self.env['purchase.order.line'].search([('account_analytic_id','=',line.account_analytic_id.id),('product_id','=',line.product_id.id),('id','!=', line.id)])
                                        total_product_purchases = 0
                                        if purchase_order_line_ids:
                                            for po_lines in purchase_order_line_ids:
                                                date_order_line = dateutil.parser.parse(str(po_lines.order_id.date_order)).date()
                                                if budget_line.general_budget_id and budget_line.general_budget_id.detail_ids and date_order_line >= budget_line.date_from and date_order_line <= budget_line.date_to:
                                                    total_product_purchases += po_lines.price_total
                                        total_product = line.price_total + total_product_purchases
                                        if total_product > detail_line.valor:
                                            raise ValidationError(_('Limite de producto ' + str(line.product_id.name)))
        return res
