from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import CommentForm
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
    comments = comment.objects.filter(truyen=id)
    context = {
        'truyens' : truyens,
        'cts': ct,
        'chapters' : chapters,
        'comments' : comments,
    }
    return render(request, 'summary/nav.html',context)

def doc(request):
    id = request.GET.get('id','') 
    chapters = chapter.objects.filter(id = id)
    context = {
        'chapters' : chapters,
    }
    return render(request, 'summary/doc.html',context)
                                  
def cmt(request):
    id = request.GET.get('id','') 
    cmt = get_object_or_404(truyen, id=id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, user=request.user, truyen=truyen)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        return render(request, 'home/login.html')
    return render(request, "summary/nav.html", {"cmt": cmt, "form": form})