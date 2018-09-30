from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " | " + self.name