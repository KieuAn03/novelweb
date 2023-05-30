from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db.models import Q # new
from django.core.paginator import Paginator


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

def doc(request):
    
    id = request.GET.get('id')
    chapters = chapter.objects.filter(id = id)
    truyens = truyen.objects.filter(id = chapters[0].truyen.id)
    list_chapter = chapter.objects.filter(truyen = truyens[0].id)
    
    context = {
        'chapters' : chapters,
        'listchapers':list_chapter,
     
    }
    return render(request, 'summary/doc.html',context)

def search (request):
    if request.method == 'GET':
        search = request.GET.get('scontent')
        truyens = truyen.objects.filter(Q(title=search) | Q(author=search))
        
        tops = truyen.objects.all().order_by('-view_count')[:3]
        context = {
            'truyens' : truyens,
            'tops' : tops
        }
        return render(request, 'home/search.html', context)
