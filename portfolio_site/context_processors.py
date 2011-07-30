from portfolio_site.portfolio.models import *


def mysitevars(request):
    site_categories = PortfolioCategory.objects.all()
    return {'SITE_CATEGORIES': site_categories}