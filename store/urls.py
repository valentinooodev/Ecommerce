from django.urls import path

from . import views
import store

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all-product'),
]
