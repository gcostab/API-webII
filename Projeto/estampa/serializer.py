from .models import Estampa
from rest_framework import serializers

# Serializers define the API representation.
class EstampaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estampa
        fields = '__all__'