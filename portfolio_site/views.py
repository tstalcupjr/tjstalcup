from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio_site.portfolio.models import *


def home_page(request):
	return render_to_response('home_page.html', {}, context_instance=RequestContext(request))
	
