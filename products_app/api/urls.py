from django.conf.urls import url
from products_app.api.views import (
    InStockUpadteView,
    AddProductView
    )

urlpatterns = [
    url(r'^instock/update/(?P<pk>[0-9]+)/$', InStockUpadteView.as_view(), name='instock-update-api'),
    url(r'^add/product/$', AddProductView.as_view(), name='add-product'),
]