from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'taxed_item',
            'available_stock',
            'discount',
        )
        model = Item