# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from catalog.models import Client


KIND_PRODUCTS = (
    ('bra', 'Бра'),
    ('lustr_ceil', 'Потолочная люстра'),
    ('lustr_hang', 'Подвесная люстра'),
    ('torch', 'Торшер'),
    ('table_lamp', 'Настольная лампа'),
    ('bulb', 'Лампочка'),
)


class Interval(object):
    def __init__(self, begin, end):
        if begin < end:
            self.begin = begin
            self.end = end
        else:
            raise ValueError

    def len(self):
        return self.end - self.begin


class IntervalWidgets(widgets.MultiWidget):
    def __init__(self, attrs_input=None, attrs_widg=None):
        _widgets = (
            widgets.TextInput(attrs_input),
            widgets.TextInput(attrs_input),
        )
        super(IntervalWidgets, self).__init__(_widgets, attrs_widg)

    def decompress(self, value):
        if value:
            return [value.begin, value.end]
        else:
            return [None, None]


class IntervalField(forms.MultiValueField):
    def __init__(self, widg=None, kind=None, attr=None):
        super(IntervalField, self).__init__(fields=(kind(attr), kind(attr)), widget=widg)

    def compress(self, data_list):
        if not (len(data_list) == 2):
            raise ValueError
        try:
            interval = Interval(data_list[0], data_list[1])
        except ValueError:
            interval = Interval(data_list[1], data_list[0])
        return interval


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client


class ProductForm(forms.Form):
    price = IntervalField(widg=IntervalWidgets, kind=forms.DecimalField, attr={'max_digits': 8, 'decimal_places': 2})
    kind = forms.MultipleChoiceField(choices=KIND_PRODUCTS, widget=widgets.CheckboxSelectMultiple)
