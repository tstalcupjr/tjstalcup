from django.conf.urls.defaults import patterns, include, url
from portfolio_site.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^time/$', current_datetime),
    # Examples:
    # url(r'^$', 'portfolio_site.views.home', name='home'),
    # url(r'^portfolio_site/', include('portfolio_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
