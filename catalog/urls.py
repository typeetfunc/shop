from django.conf.urls.defaults import *
from catalog.views import *

urlpatterns = patterns('',
	url(r'^$', catalog_index),
	url(r'^product/$', show_product),
	)