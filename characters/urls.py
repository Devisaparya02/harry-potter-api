from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, HouseViewSet

# Create a router for the ViewSets
router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'houses', HouseViewSet)

# Include the router-generated URLs
urlpatterns = [
    path('', include(router.urls)),
]
