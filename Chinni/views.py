from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def two(request):
    return HttpResponse('This is my one and only secpond FBV')

def work(request):
    return render(request,'work.html')