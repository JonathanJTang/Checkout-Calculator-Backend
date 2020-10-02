from django.shortcuts import render

from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ListItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DetailItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer