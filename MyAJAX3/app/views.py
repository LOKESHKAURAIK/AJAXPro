from django.shortcuts import render
from .models import Student
def index(request):
    return render(request,"index.html")

def ajaxdata(request):
    data=request.GET['q']
    #res = Student.objects.filter(sname=data)             # According to name
    res = Student.objects.filter(sname__contains=data)     # According to first alphabate of name
    # res = Student.objects.filter(email=data)              # According to email
    return render(request,"ajaxdata.html",{"res":res})