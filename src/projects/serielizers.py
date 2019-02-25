from rest_framework import serializers
from .models import Task, Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'url', 'name', 'description','start_date','due_date','leader','leader_email')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'url', 'project_name' , 'name', 'assignee','assignee_email','start_date','due_date','completed','notes')