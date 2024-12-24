from django.urls import path
from .views import *
urlpatterns=[
    path('', home, name='home'),
    path('contact/',contact,name='contact'),
    path('mode/',mode,name='mode'),
    path('add-category/',add_category,name='add_category'),
    path('add-product/',AddProduct.as_view(),name='add_product'),
    path('products/',Products.as_view(),name='products')
]
