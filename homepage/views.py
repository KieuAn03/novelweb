from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
    truyens = truyen.objects.all()
    tops = truyen.objects.all().order_by('-view_count')[:3]
    context = {
        'truyens' : truyens,
        'tops' : tops
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

