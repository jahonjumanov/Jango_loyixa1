from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def salom(request): #request->so'rov
    return HttpResponse("Hello World")


