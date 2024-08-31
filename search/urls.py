from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    # Route to render the home page
    path('', views.home, name='home'),

    # Route to render the search page
    path('search/', views.search_page, name='search_page'),

    # Route to handle search requests via AJAX
    path('search-items/', views.search_items, name='search_items'),

    # API endpoint for CRUD operations on ClothingItem
    path('api/', include(router.urls)),
]
