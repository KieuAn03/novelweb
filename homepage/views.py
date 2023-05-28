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

def deltail(request):
    id = request.GET.get('id','') 
    truyens = truyen.objects.filter(id=id)
    ct = truyen_category.objects.filter(Truyen = id)
    chapters = chapter.objects.filter(truyen = id)
    context = {
        'truyens' : truyens,
        'cts': ct,
        'chapters' : chapters,
    }
    return render(request, 'summary/nav.html',context)

def doc(request):
    id = request.GET.get('id','') 
    chapters = chapter.objects.filter(id = id)
    context = {
        'chapters' : chapters,
    }
    return render(request, 'summary/doc.html',context)
