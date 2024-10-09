from django.db import models



class Search(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phonenum = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
