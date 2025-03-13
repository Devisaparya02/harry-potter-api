from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, HouseViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'houses', HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
