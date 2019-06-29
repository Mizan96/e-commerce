from django.conf.urls import url
from cart_app.api import views

urlpatterns = [
    url(r'^add-cart/(?P<pk>[0-9]+)/$', views.CartApiView.as_view() ,name='add-cart'),
]