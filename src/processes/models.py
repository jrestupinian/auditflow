from django.db import models

# Create your models here.

class MacroProcess(models.Model):
    name            = models.CharField(max_length=160)
    created_at      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Process(models.Model):
    macroprocess_name   = models.ForeignKey(MacroProcess, on_delete=models.PROTECT)
    name                = models.CharField(max_length=160)
    objective           = models.TextField()
    reach               = models.TextField()
    applies_to          = models.TextField()
    localization        = models.TextField()
    leader              = models.CharField(max_length=160)