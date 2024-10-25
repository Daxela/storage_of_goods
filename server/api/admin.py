from django.contrib import admin
from .models import Product, Price, Type

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'barcode', 'date_of_update', 'type')
    date_hierarchy = 'date_of_update'
    search_fields = ['name', 'price__cost', 'price__currency', 'quantity', 'barcode', 'type__name']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('cost', 'currency')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')