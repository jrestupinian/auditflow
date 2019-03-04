from rest_framework import serializers
from .models import Risk, RiskType

class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskType
        fields = ('id', 'url', 'name', 'definition')

class RiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'url', 'risktype_name' ,'name', 'reference', 'description')