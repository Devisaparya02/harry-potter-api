from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Character, House
from .serializers import CharacterSerializer, HouseSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'role', 'house__name']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data, content_type='application/json')

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
