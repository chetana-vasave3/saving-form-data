from django.http import HttpResponse
from saveform.models import Saveform

from django.shortcuts import render
def saveinquery(request):
    #return HttpResponse("welcome")
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        data=Saveform(name=name,email=email,message=message)#get data
        data.save()#save data
    return render(request,"inquiryform.html")