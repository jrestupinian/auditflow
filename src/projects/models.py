from django.db import models

# Create your models here.
class Project(models.Model):
    name            = models.CharField(max_length=160)
    description     = models.TextField()
    start_date      = models.DateField()
    due_date        = models.DateField()
    leader          = models.CharField(max_length=160)
    leader_email    = models.EmailField()
    created_at      = models.DateTimeField(auto_now_add=False)
    last_modified   = models.DateTimeField(auto_now=True)

class Task(models.Model):
    project_name    = models.ForeignKey(Project, on_delete=models.CASCADE)
    name            = models.CharField(max_length=160)
    assignee        = models.CharField(max_length=160)
    assignee_email  = models.EmailField()
    start_date      = models.DateTimeField()
    due_date        = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=False)
    last_modified   = models.DateTimeField(auto_now=True)
    completed       = models.DateTimeField()
    notes           = models.TextField()



