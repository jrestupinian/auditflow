from django.shortcuts import render
from rest_framework import viewsets
from .models import Process, MacroProcess
from .serielizers import ProcessSerializer, MacroProcessSerializer

class MacroProcessView(viewsets.ModelViewSet):
    queryset = MacroProcess.objects.all()
    serializer_class = MacroProcessSerializer

class ProcessView(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer