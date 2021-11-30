from os import name
from django.urls import path
from . import views
from .views import (
    CategoryDetailView,
    ProductDetailView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('iphone/', views.iphone, name='iphone'),
    path('ipad/', views.ipad, name='ipad'),
    path('macbook/', views.macbook, name = 'macbook'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]