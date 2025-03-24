from django.urls import path
from .views import *
urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('contact/',contact,name='contact'),
    path('mode/',mode,name='mode'),
    path('add-category/',add_category,name='add_category'),
    path('add-product/',AddProduct.as_view(),name='add_product'),
    path('products/',Products.as_view(),name='products'),
    path('sellers/',Sellers.as_view(),name='sellers'),
    path('product/<slug:product_slug>/',DProducts.as_view(),name='product'),
    path('seller/<slug:seller_slug>/',Seller.as_view(),name='seller'),
    path('login/',Login.as_view(),name='login'),
    path('registration/',register,name='register'),
    path('logout/',logoutv,name='logout')
]
