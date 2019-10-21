from django.shortcuts import render
from shiwake.forms import Postform
from django.http import HttpResponse

def formdata():
      if request.method == "POST":
            f = Postform(request.POST)
            if form.is_valid():
                  return redirect('result')
      else:
            f = Postform()
      
      return render(request,'shiwake/shiwakeform.html',{'form1':f})

def result():
      return render(request,
                    'shiwake/result.html',{})
