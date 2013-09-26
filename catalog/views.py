# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def catalog_index(request):
	return render_to_response("catalog/catalog-index.htm")
def show_product(request):
	return render_to_response("catalog/product.htm")