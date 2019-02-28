from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256, unique=True)
    number = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name