from operator import truediv
from pickle import TRUE
from django.db import models

class Post(models.Model):
    location = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    head = models.IntegerField(default=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item