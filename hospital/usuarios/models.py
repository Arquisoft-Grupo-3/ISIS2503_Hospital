from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)