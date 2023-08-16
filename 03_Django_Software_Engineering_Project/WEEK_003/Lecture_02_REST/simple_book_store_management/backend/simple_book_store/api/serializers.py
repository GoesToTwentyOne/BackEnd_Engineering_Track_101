from rest_framework import serializers
from api.models import BookStoreModel
class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookStoreModel
        fields='__all__'
    