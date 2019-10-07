from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale

from odoo import http


class CustomWebsite(Website):
    def index(self, **kw):
        pass


class CustomWebsiteSale(WebsiteSale):
    def sitemap_shop(env, rule, qs):
        super().sitemap_shop(env, rule, qs)

    @http.route([
        '''/''',
        '''/page/<int:page>''',
        '''/category/<model("product.public.category"):category>''',
        '''/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        return super().shop(page=page, category=category, search=search, ppg=ppg, **post)

    @http.route(['/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        return super().product(product, category=category, search=search, **kwargs)
