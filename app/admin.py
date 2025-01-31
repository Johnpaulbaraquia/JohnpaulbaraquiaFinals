from django.contrib import admin
from .models import Categories, Customer, Supplier, Order, Product, OrderItem, OrderDetail


admin.site.register(Categories)

admin.site.register(Customer)

admin.site.register(Supplier)

admin.site.register(Order)

admin.site.register(Product)

admin.site.register(OrderItem)

admin.site.register(OrderDetail)


# Register your models here.
