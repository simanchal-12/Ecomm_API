from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category
        
class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields = (
            'id',
            'name',
            'category',
            'price',
            'available',
            'img_url',
            'created_by',
            'status',
            'date_created'
        )
        model = Product