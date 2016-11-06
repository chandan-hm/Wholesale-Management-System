from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$', views.login, name='login'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^producer$', views.producer, name='producer'),

    url(r'^index$', views.index, name='index'),

    url(r'^producer/(?P<producer_id>[0-9]+)/$', views.detail_producer, name='detail_producer'),

    url(r'^customer$', views.customer, name='customer'),

    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.detail_customer, name='detail_customer'),

    url(r'^product$', views.product, name='product'),

    url(r'^product/(?P<product_id>[0-9]+)/$', views.detail_product, name='detail_product'),

    url(r'^payment$', views.payment, name='payment'),
]
