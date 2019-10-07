from odoo.addons.http_routing.models.ir_http import slug

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _compute_website_url(self):
        """ Override function. Modify product url for website sale purpose. """
        super()._compute_website_url()
        for product in self:
            product.website_url = '/product/%s' % slug(product)
