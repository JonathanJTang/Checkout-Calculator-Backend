from django.shortcuts import render

from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


# Only allows GET
class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
# Allows GET, PUT, PATCH
class DetailItem(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    