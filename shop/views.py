# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from catalog.forms import ClientForm, ProductForm
from catalog.models import *


def index(request):
	return render_to_response('index.htm')

def show_catalog(request):
    if request.method == 'GET':
        f = ProductForm(request.GET)
        if f.is_valid():
            cd = f.cleaned_data
            products = Product.objects.filter(price__range=(cd['price'].begin, cd['price'].end)).order_by('price')
            products_group_by_kind = [{'name': kind, 'set': products.filter(kind=kind)}
                                      for kind in cd['kind']]
            return render_to_response('catalog/catalog.htm', {'form': f, 'groups_products': products_group_by_kind})
        else:
            return render_to_response('catalog/catalog.htm', {'form': f})
    else:
        return render_to_response('catalog/catalog.htm',{'form': ProductForm()})
