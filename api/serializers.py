from rest_framework import serializers
from .models import Collection, BestSeller, Shop


class CollectionSerializer(serializers.ModelSerializer):
    formatted_price = serializers.SerializerMethodField()
    class Meta:
        model = Collection
        fields = '__all__' 

    def get_formatted_price(self, obj):
        return obj.formatted_price()  # Call the method from the model


class BestSellerSerializer(serializers.ModelSerializer):
    formatted_price = serializers.SerializerMethodField()

    class Meta:
        model = BestSeller
        fields = '__all__'

    def get_formatted_price(self, obj):
        return obj.formatted_price()  # Call the method from the model



class ShopSerializer(serializers.ModelSerializer):
    formatted_price = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields = ['id', 'title', 'price', 'image', 'category', 'type', 'formatted_price']

    def get_formatted_price(self, obj):
        return obj.formatted_price() 