from django.conf.urls import url
from accounts_app import views


urlpatterns =[
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.register_view, name='signup'),
    url(r'^verification/(?P<username>[\w-]+)/$', views.verification_view, name='email_verfication'),
    url(r'^successful/$', views.successful_view, name='email_successful'),

]