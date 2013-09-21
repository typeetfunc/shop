from django import forms
from django.forms import widgets
from catalog.models import Clients


KIND_OF_PRODUCT = (
    ('bra', 'Бра'),
    ('lustre',
     (
         ('ceil_lust', 'Потолочная люстра'),
         ('pend_lust', 'Подвесная люстра'),
     )
    ),
    ('bulb', 'Лампочка'),
    ('t_lamp', 'Настольная лампа'),
    ('torch', 'Торшер'),
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
            return [self.begin, self.end]
        else:
            return [None, None]


class IntervalField(forms.MultiValueField):
    def __init__(self, widgets, field_cons, *args):
        super(IntervalField, self).__init__(fields=(field_cons(*args), field_cons(*args))), widgets)

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
        model = Clients


class ProductForm(forms.Form):
    price = IntervalField(IntervalWidgets, forms.DecimalField, 8, 2)
    kind = forms.MultipleChoiceField(choices=KIND_OF_PRODUCT, widget=widgets.CheckboxSelectMultiple)
