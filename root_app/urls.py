from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from home_app import views

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
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
