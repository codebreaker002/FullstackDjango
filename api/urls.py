from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ItemViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', ItemViewSet)

# Add custom endpoints for item filtering with query parameters:
urlpatterns = [
    path('', include(router.urls)),
]