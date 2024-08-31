from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import ClothingItem
from .serializers import ItemSerializer

# ViewSet for handling API requests


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ItemSerializer

# Function to render the home page with all items


def home(request):
    items = ClothingItem.objects.all()
    return render(request, 'search/home.html', {'items': items})

# Function to render the search page


def search_page(request):
    return render(request, 'search/home.html')

# Function to handle search requests


def search_items(request):
    query = request.GET.get('query', '')
    if len(query) > 3:
        items = ClothingItem.objects.filter(name__icontains=query)
        results = [
            {
                "name": item.name,
                "description": item.description,
                "price": str(item.price),
                "image": item.image.url if item.image else ''
            }
            for item in items
        ]
    else:
        results = []
    return JsonResponse(results, safe=False)
