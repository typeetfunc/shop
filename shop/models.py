from django.db import models


class Products (models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveSmallIntegerField()
    balance = models.PositiveSmallIntegerField()
    description = models.TextField()
    image = models.ImageField()


class Map_orders_products (models.Model):
    product = models.ForeignKey(Products)
    amount = models.PositiveSmallIntegerField()
    order = models.ForeignKey(Orders)


class Orders (models.Model):
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Clients)


class Clients (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    ip = models.IPAddressField()






