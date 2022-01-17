from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='base_view'),
    path('store_main_page', views.store_main_page, name='store_main_page'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('test', views.test, name='test'),
    path('load-more-posts/', DynamicPostLoad.as_view(), name='load_more_posts')
    ]
