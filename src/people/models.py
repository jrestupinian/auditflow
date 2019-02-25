from django.db import models

# Create your models here.
class Person(models.Model):
    name =      models.CharField(max_length=150)
    email =     models.EmailField() 
    class Meta:
        verbose_name_plural = "people"
    
    def __str__(self):
        return self.name