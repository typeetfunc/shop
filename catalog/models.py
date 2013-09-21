from django.db import models
# -*- coding: utf-8 -*-
KIND_PRODUCTS = (
    ('bra', 'Бра'),
    ('lustre',
        (
            ('lustr_ceil', 'Потолочная люстра'),
            ('lustr_hang', 'Подвесная люстра'),
        )
    ),
    ('torch', 'Торшер'),
    ('table_lamp', 'Настольная лампа'),
    ('bulb', 'Лампочка'),
)
STATUS = (
    ('issued', 'Оформлен'),
    ('adopted', 'Принят'),
    ('deliev', 'Доставлен'),
)


class Products (models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=10, choices=KIND_PRODUCTS)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    balance = models.PositiveSmallIntegerField()
    description = models.TextField()
    #image = models.ImageField()


class Clients (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=50, null=True, blank=True)
    ip = models.IPAddressField(null=True, blank=True)


class Orders (models.Model):
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Clients)
    status = models.CharField(max_length=10, choices=STATUS, default='issued')


class Map_orders_products (models.Model):
    product = models.ForeignKey(Products)
    amount = models.PositiveSmallIntegerField()
    order = models.ForeignKey(Orders)









