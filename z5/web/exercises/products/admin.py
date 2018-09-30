from django.contrib import admin
from products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'is_available']
    search_fields = ['name', 'description']
    list_filter = ['is_available']


admin.site.register(Product, ProductAdmin)
