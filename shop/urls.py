from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^catalog/', include('catalog.urls')),
	# Examples:
	# url(r'^$', 'shop.views.home', name='home'),
	# url(r'^shop/', include('shop.foo.urls')),


	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()