from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product, Customer, Order, OrderItem, Address, Cart, CartItem

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'unit_price',
            'photos',
            'price_with_tax',
        )
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


        
class ProductRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'unit_price',
            'inventory',
            'last_update'
        )

