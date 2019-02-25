from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Project
from .serielizers import TaskSerializer, ProjectSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Taskview(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer