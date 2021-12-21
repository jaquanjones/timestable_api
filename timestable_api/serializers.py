from rest_framework.serializers import ModelSerializer

from categories.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'
        fields = '__all__'
