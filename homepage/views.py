from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
    truyens = truyen.objects.all()
    context = {
        'truyens' : truyens
    }
    return render(request,'home/index.html',context)

def summary(request):
    return render(request, 'summary/nav.html')