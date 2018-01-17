from rest_framework import serializers

from core.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'nutrition_value', 'picture', 'id']
        read_only_fields = ['id']
