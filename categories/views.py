from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from timestable_api.serializers import CategorySerializer
from .models import Category


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/categories/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of categories'
        },
        {
            'Endpoint': '/categories/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single category',
        },
        {
            'Endpoint': '/categories/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new category'
        },
        {
            'Endpoint': '/categories/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sentin'
        },
        {
            'Endpoint': '/categories/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_category(request):
    data = request.data
    category = Category.objects.create(
        body=data['body']
    )
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_category(request, pk):
    data = request.data
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Note Successfully deleted')
