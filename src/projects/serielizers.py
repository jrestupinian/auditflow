from rest_framework import serializers
from .models import Task, Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    project_status = serializers.CharField(source='get_project_status_display')
    class Meta:
        model = Project
        fields = ('id', 'url', 'name', 'description','start_date','due_date', 'project_status','leader','leader_email')
        depth = 1

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'url', 'project_name' , 'name', 'assignee','assignee_email','start_date','due_date','completed','notes')
        depth = 0