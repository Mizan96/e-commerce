from django.conf.urls import url
from home_app.views import home_view

urlpatterns =[
    url(r'^$', home_view, name='home'),
]