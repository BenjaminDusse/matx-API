from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from store.models import *
from store.serializers import CollectionSerializer, ProductSerializer, ProductRelationSerializer
from store.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from store.pagination import DefaultPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['title', 'description']
    pagination_class = DefaultPagination

    
    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': "Product cannot deleted because it is assosiated with an order item"})
        return super().destroy(request, *args, **kwargs)



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count = Count("product")).all()
    serializer_class = CollectionSerializer

    def destroy(self, request):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot deleted because it is assosiated with an order item'})
        return super().destroy(request, *args, **kwargs)
