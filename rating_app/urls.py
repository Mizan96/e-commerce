from django.conf.urls import url
from rating_app import views

urlpatterns =[
    url(r'^api/$', views.rating_api_view,name='rating-api'),
]