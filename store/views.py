from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from store.models import *
from store.serializers import CollectionSerializer

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count = Count("product")).all()
    serializer_class = CollectionSerializer


