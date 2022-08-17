from django.db import models

class Post(models.Model):
    area = models.CharField(max_length=100, default='노원구')
    location = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    head = models.IntegerField(default=2)
    photo = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item