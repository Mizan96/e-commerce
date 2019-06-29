from django.conf.urls import url
from search_app import views

urlpatterns = [
    url(r'^$', views.search_view, name='home'),
]