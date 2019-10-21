from django.urls import path
from . import views

urlpatterns = [
      path('',views.formdata,name='formdata'),
      path('result/',views.result,name='result'),
      ]
