# views.py
from rest_framework import generics
from .models import Collection
from .serializers import CollectionSerializer
from .models import BestSeller
from .serializers import BestSellerSerializer
from .models import Shop
from .serializers import ShopSerializer


class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    
    

class BestSellerList(generics.ListAPIView):
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializer 
    
    
    
class ShopSellerList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer       
    
    
    
    
    
# # views.py
# class RelatedProductsView(generics.ListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         product_id = self.kwargs['product_id']
#         product = Product.objects.get(id=product_id)
#         # Fetch related products based on category or subcategory, excluding the current product
#         return Product.objects.filter(category=product.category).exclude(id=product.id)
   