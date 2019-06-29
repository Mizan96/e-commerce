from django.conf.urls import url, include
from products_app import views
urlpatterns = [
    url(r'^category/(?P<pk>[0-9]+)/$', views.all_products_in_a_category_view,
                                          name='all_products_in_a_category'),
    url(r'^product/details/(?P<pk>[0-9]+)/$', views.individual_product_detail_view,
                                          name='individual_product_detail'),
    url(r'^product/add/$', views.product_add, name='product_add'),
    url(r'^api/', include('products_app.api.urls',namespace='prpduct-api')),
    url(r'^best-selling/$', views.best_selling_view ,name='best-selling'),
    url(r'^fetured/$', views.featured_view ,name='fetured'),
    url(r'^latest/$', views.latest_view ,name='latest')
    # url(r'^detail/api/$', views.product_detail_api, name='product-detail-api'),
]
