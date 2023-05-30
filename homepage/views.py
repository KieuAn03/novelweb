from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import *
from .forms import CommentForm
from datetime import datetime
from django.db.models import Q # new

import json
from django.db.models import Q # new

def index(request):
    truyens = truyen.objects.all()
    tops = truyen.objects.all().order_by('-view_count')[:3]
    context = {
        'truyens' : truyens,
        'tops' : tops
    }
    return render(request,'home/index.html',context)

def deltail(request):
    """
    hàm lấy dữ liệu thể loại, tên truyện, số chương, chương truyện, để đưa lên web
    """
    id = request.GET.get('id','') 
    truyens = truyen.objects.filter(id=id)
    ct = truyen_category.objects.filter(Truyen = id)
    chapters = chapter.objects.filter(truyen = id)
    num_chap = chapter.objects.filter(truyen = id).count()
    num_cmt = comment.objects.filter(truyen=id).count()
    context = {
        'truyens' : truyens,
        'cts': ct,
        'chapters' : chapters,
        'num_cmt' : num_cmt,
        'num_chap' : num_chap,
    }
    return render(request, 'summary/nav.html',context)

def doc(request):
    """
    load chương truyện lên web để đọc
    """
    id = request.GET.get('id')
    chapters = chapter.objects.filter(id = id)
    context = {
        'chapters' : chapters,
    }
    return render(request, 'summary/doc.html',context)


# add comment and delete comment
def add_comment(request):
    """
        thêm bình luận cho 1 truyện
    """
    pk=request.GET.get('id')
    eachComment = truyen.objects.get(id=pk)
    form = CommentForm(instance=eachComment) 
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachComment)
        if form.is_valid():
            body = form.cleaned_data['content']
            c = comment(truyen=eachComment,user=request.user ,content=body,date_published=datetime.now())
            c.save()
            return redirect('homepage')
        else:
            print('form is invalid')
    else:
        form = CommentForm()
    context = {
        'form' : form ,
    }
    return render(request, "summary/add_cmt.html", context)

def delete_comment(request):
    """
    xoá binh luận gần nhất của 1 truyện
    """
    pk=request.GET.get('id')
    comments = comment.objects.filter(truyen=pk).last()
    comments.delete()
    return redirect('homepage')

def likeTruyen(request):
    """
    thêm truyện yêu thích
    """
    id=request.GET.get('id')
    users = request.user
    truyens = truyen.objects.get(id=id)
    if not favorate.objects.filter(truyen=truyens,user=users):
        c = favorate(truyen=truyens,user=request.user)
        c.save()
    return redirect('favorite')

def truyenFavo(request):
    users = request.user
    favorates = favorate.objects.filter(user=users)
    context = {
        'favorates' : favorates,
    }
    return render(request,'summary/fav.html',context)

def search (request):
    if request.method == 'GET':
        search = request.GET.get('scontent')
        truyens = truyen.objects.filter(Q(title=search) | Q(author=search))
        context = {
            'truyens' : truyens,
        }
        return render(request, 'home/search.html', context)

def delete_favo(request):
    """
    xoá truyện khỏi mục yêu thích
    """
    id=request.GET.get('id')
    favorates = favorate.objects.filter(id=id)
    favorates.delete()
    return redirect('favorite')