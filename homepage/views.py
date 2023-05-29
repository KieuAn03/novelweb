from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
<<<<<<< HEAD
from .forms import CommentForm
from datetime import datetime
=======
from django.db.models import Q # new

>>>>>>> c6b8b5eb067ae235b34506223ebbbca7bb99ad08
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
    context = {
        'chapters' : chapters,
    }
    return render(request, 'summary/doc.html',context)
<<<<<<< HEAD
                                  
def add_comment(request):
    pk=request.GET.get('id')
    eachComment = truyen.objects.get(id=pk)
    form = CommentForm(instance=eachComment) 
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachComment)
        if form.is_valid():            
            name = request.user.username
            passw = request.user.password
            body = form.cleaned_data['content']
            c = comment(truyen=eachComment, user=authenticate(request,username = name,password = passw),content=body,date_published=datetime.now())
            c.save()
            return redirect('summary/nav')
        else:
            print('form is invalid')
    else:
        form = CommentForm()
    context = {
        'form' : form
    }
    return render(request, "summary/add_cmt.html", context)
=======

def search (request):
    if request.method == 'GET':
        search = request.GET.get('scontent')
        truyens = truyen.objects.filter(Q(title=search) | Q(author=search))
        context = {
            'truyens' : truyens,
        }
        return render(request, 'home/search.html', context)
>>>>>>> c6b8b5eb067ae235b34506223ebbbca7bb99ad08
