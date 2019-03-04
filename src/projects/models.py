from django.db import models
from people.models import Person
# Create your models here.
class Project(models.Model):
    name            = models.CharField(max_length=160)
    description     = models.TextField()
    start_date      = models.DateField()
    due_date        = models.DateField()
    leader          = models.ForeignKey(Person, on_delete=models.PROTECT)
    leader_email    = models.EmailField()
    created_at      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    project_name    = models.ForeignKey(Project, on_delete=models.PROTECT)
    name            = models.CharField(max_length=160)
    assignee        = models.ForeignKey(Person, on_delete=models.PROTECT)
    assignee_email  = models.EmailField()
    start_date      = models.DateField()
    due_date        = models.DateField()
    created_at      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)
    completed       = models.DateField(default=None, blank=True, null=True)
    notes           = models.TextField()

    def __str__(self):
        return self.name



