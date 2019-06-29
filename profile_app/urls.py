from django.conf.urls import url
from profile_app import views
urlpatterns = [
    url(r'^$', views.profile_view ,name='home'),
    url(r'^history/$', views.history_view ,name='history'),
    url(r'^history/order/(?P<pk>[0-9]+)/$', views.order_view , name='order'),
]