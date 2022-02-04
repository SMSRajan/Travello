from django.db import models


class Destination(models.Model):
    id: int
    name: str
    image: str
    desc: str
    price: int
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


# Create your models here.
