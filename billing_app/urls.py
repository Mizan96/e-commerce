from django.conf.urls import url
from billing_app import views

urlpatterns =[
    url(r'^$', views.billing_view, name='home'),
    url(r'^confirm/$', views.confirm_view , name='confirm')
]
