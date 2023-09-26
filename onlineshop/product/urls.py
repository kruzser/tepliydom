from django.urls import path, include

from .views import LatestProductsList, ProductDetail, CategoryDetail, CategoryLits, FiltersList, getBrandList
from .views import search

urlpatterns = [
    path('latest-products/<slug:per_page>/<slug:page>', LatestProductsList.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
    path('products/<slug:category_slug>/<slug:per_page>/<slug:page>', CategoryDetail.as_view()),
    path('category/', CategoryLits.as_view()),
    path('filters/<slug:category_slug>', FiltersList.as_view()),
    path('get_brands/', getBrandList.as_view()),
]