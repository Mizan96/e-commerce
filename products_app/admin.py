from django.contrib import admin
from products_app.models import ProductCategory, IndividualProduct
# Register your models here.
from pagedown.widgets import AdminPagedownWidget
from django.db import models

class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(ProductCategory)
admin.site.register(IndividualProduct, AlbumAdmin)
