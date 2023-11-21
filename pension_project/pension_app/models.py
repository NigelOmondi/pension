from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    pension_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

