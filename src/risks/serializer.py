from rest_framework import serializers
from .models import Risk

class RiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'url', 'name', 'reference', 'description')