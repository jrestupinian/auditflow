from django.shortcuts import render
from rest_framework import viewsets
from .models import Risk, RiskType
from .serializer import RiskSerializer, RiskTypeSerializer


# Create your views for risk.

class RiskTypeView(viewsets.ModelViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer

class RiskView(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

