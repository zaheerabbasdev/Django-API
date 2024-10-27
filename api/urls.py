# urls.py
from django.urls import path
from .views import CollectionList, BestSellerList, ShopSellerList

urlpatterns = [
    path('collections/', CollectionList.as_view(), name='collection-item-list'),
    path('bestsellers/', BestSellerList.as_view(), name='bestseller-list'),
    path('shops/', ShopSellerList.as_view(), name='shop-list'),
]
