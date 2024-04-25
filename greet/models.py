from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    birthyear = models.IntegerField(default=1970)

    def __str__(self):
        return self.name
    