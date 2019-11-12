from django.shortcuts import render
from .forms import Postform
from django.http import HttpResponse
from django.http import HttpResponseRedirect as redirect

global month
global day
global tekiyou_kari
global tekiyou_kasi
global tekiyou_com
global amount_kari
global amount_kasi

def formdata(request):
      if request.method == "POST":
            f = Postform(request.POST)
            if f.is_valid():
                  month = request.POST.get("month","")
                  day = request.POST.get("day","")
                  tekiyou_kari = request.POST.get("tekiyou_kari","")
                  tekiyou_kasi = request.POST.get("tekiyou_kasi","")
                  tekiyou_com = request.POST.get("tekiyou_com","")
                  amount_kari = request.POST.get("amount_kari","")
                  amount_kasi = request.POST.get("amount_kasi","")
                  dd = open('.\\shiwake\\dicdic.py','w')
                  dd.write('ddd = {"month":' + month + ',\n"day":' + day + ',\n"tekiyou_kari":"' + tekiyou_kari + '",\n"tekiyou_kasi":"' + tekiyou_kasi + '",\n"tekiyou_com":"' + tekiyou_com + '",\n"amount_kari":' + amount_kari + ',\n"amount_kasi":' + amount_kasi + '}')
                  dd.close()
                  from . import app
                  return redirect('result')
      else:
            f = Postform()
      
      return render(request,
                    'shiwake/shiwakeform.html',{'form1':f})

def result(request):
      return render(request,
                    'shiwake/result.html',{})
