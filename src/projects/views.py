from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Task, Project

class IndexView(generic.ListView):
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return the las five projects"""
        return Project.objects.order_by('-created_at')[:5]

class DetailView(generic.DetailView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(created_at__lte=timezone.now())