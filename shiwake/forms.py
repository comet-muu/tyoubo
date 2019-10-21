from django.db import models
from django.conf import settings
from django.utils import timezone

class Postform(forms.Form):
      month = forms.CharField(max_length=10)
      day = forms.CharField(max_length=10)
      tekiyou_kari = forms.CharField(max_length=10)
      tekiyou_kasi = forms.CharField(max_length=10)
      tekiyou_com = forms.TextField()
      amount_kari = forms.IntegerField()
      amount_kasi = forms.IntegerField()
