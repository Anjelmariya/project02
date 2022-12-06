from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to=250)
    desc=models.TextField()

    def __str__(self):
        return self.name

class People(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to=250)
    desc1 = models.TextField()

    def __str__(self):
        return self.name1
