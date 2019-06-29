from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from home_app import views


from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete)

urlpatterns = [
    # @login_required
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts_app.urls', namespace='accounts')),
    url(r'^products/', include('products_app.urls', namespace='products')),
    url(r'^carts/', include('cart_app.urls', namespace='cart')),
    url(r'^rating/', include('rating_app.urls', namespace='rating')),
    url(r'^search/', include('search_app.urls', namespace='search')),
    url(r'^billing/', include('billing_app.urls', namespace='billing')),
    url(r'^shipping/', include('shipping_app.urls', namespace='shipping')),
    url(r'^profile/', include('profile_app.urls', namespace='profile')),
    url(r'^wish/', include('wish_app.urls', namespace='wish')),
    url(r'^404/$', views.not_found_view, name='404-page'),
    url(r'^$', views.home_view, name='home'),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'reset-password/complete/$', password_reset_complete,
        name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
