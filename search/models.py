from django.db import models



class BioData(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phonenum = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='search_images/')
    ssn = models.CharField(max_length=11, blank=True, null=True)


    def __str__(self):
        return self.name
