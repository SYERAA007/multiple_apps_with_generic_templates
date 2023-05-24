from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def one(request):
    return HttpResponse('This is my one and only first FBV')

def two(request):
    return HttpResponse('This is my one and only secpond FBV')

def home(request):
    return render(request,'home.html')

def work(request):
    return render(request,'work.html')