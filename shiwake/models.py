from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
      month = models.CharField(max_length=10)
      day = models.CharField(max_length=10)
      tekiyou_kari = models.CharField(max_length=10)
      tekiyou_kasi = models.CharField(max_length=10)
      tekiyou_com = models.TextField()
      amount_kari = models.IntegerField()
      amount_kasi = models.IntegerField()
