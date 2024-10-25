from django.db import models


class Product(models.Model):
    name = models.TextField(blank=True)
    price = models.ForeignKey('Price', on_delete=models.CASCADE, default=None, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    # штрих код товара
    barcode = models.TextField(blank=True)
    # дата обновления записи
    date_of_update = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    # валюта(RUB, USD, EUR, ...)
    currency = models.TextField(blank=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cost} {self.currency}"
