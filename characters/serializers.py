from rest_framework import serializers
from .models import Character, House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)
    house_id = serializers.PrimaryKeyRelatedField(queryset=House.objects.all(), source='house', write_only=True)

    class Meta:
        model = Character
        fields = "__all__"

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'  # Ensure role is included

    role = serializers.CharField(required=True, allow_blank=False)