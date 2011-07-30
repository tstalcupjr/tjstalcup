from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio_site.portfolio.models import *
# Create your views here.

def index(request):
	return render_to_response('port/index.html')

def category(request, slug):
	category = PortfolioCategory.objects.get(slug=slug)
	print category
	return render_to_response('port/category.html', {'cat':category}, context_instance=RequestContext(request))  