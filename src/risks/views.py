from django.shortcuts import render
from rest_framework import viewsets
from .models import Risk
from .serializer import RiskSerializer


# Create your views for risk.

class RiskView(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

