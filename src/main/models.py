from django.db import models

class Post(models.Model):

    AREA_CHOICES = {
        ('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'), ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'), ('동대문구', '동대문구'), ('동작구', '동작구'), 
        ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'), ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랑구', '중랑구'), 
    }

    area = models.CharField(max_length=100, choices=AREA_CHOICES, default='노원구')
    location = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    head = models.IntegerField(default=2)
    photo = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item