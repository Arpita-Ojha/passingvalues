from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request,a):
    return HttpResponse('Good Morning {} '.format(a))

def hi(request,b):
    return HttpResponse(f'Good Morning {b}')
