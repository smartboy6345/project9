from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def semi(request):
    data='JEEVAN KUMAR'
    data1='at the age of 21'
    d={'page':data,'age':data1 }
    return render(request,'semidynamic.html',d)

def jeevan(request):
    data='From Giddaluru'
    
    return HttpResponse('<h1><marquee>This is one of the most great day that India won the MATCH</marquee><h1>')