from rest_framework import serializers
from advertising.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'prd_key', 'prd_name', 'prd_description',)