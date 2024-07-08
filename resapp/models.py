from django.db import models


# Create your models here.
class Contacts(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    msg = models.TextField()

    def __str__(self):
        return self.username
