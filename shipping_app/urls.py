from django.conf.urls import url
from shipping_app import views

urlpatterns =[
    url(r'^$', views.shipping_view, name='home' ),
    url(r'^order/$', views.unconfirm_order, name='order' ),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.unconfirm_detail, name='detail' ),
]