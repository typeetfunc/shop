# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def catalog_index(request):
	return render_to_response("catalog/catalog-index.htm")