from django.contrib import admin
from billing_app.models import BillingProfileModel, Order

class OrderAdmin(admin.ModelAdmin):
    search_fields = ('order_number', 'id' )

admin.site.register(BillingProfileModel)
admin.site.register(Order, OrderAdmin)

