from django.contrib import admin
from cart_app.models import Cart, CartAmount
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartAmount)
