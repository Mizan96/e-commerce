from django.conf.urls import url
from wish_app import views

urlpatterns = [
    url(r'^update/$', views.wish_update_view, name='update')
]