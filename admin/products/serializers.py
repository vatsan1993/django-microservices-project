# serializer is necessary to convert model instances into JSON format
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product # Specify the model to serialize
        fields = "__all__"  # Serialize all fields of the model

# no serializer for user model as we return id. if not  we need to create a serializer for User model