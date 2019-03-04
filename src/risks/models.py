from django.db import models

# Risk model

class RiskType(models.Model):
    name            = models.CharField(max_length=160)
    definition      = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Risk(models.Model):
    risktype_name   = models.ForeignKey(RiskType, on_delete=models.PROTECT)
    name            = models.CharField(max_length=160)
    reference       = models.CharField(max_length=100)
    description     = models.TextField()

    def __str__(self):
        return self.name
