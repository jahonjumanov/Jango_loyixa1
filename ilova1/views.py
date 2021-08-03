from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def salom(request): #request->so'rov
    mevalar = models.Meva.objects.all()
    return render(request,'index.html', {'mevalar':mevalar})



