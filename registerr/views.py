from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from. import views

# Create your views here.

# Dang ki tai khoan
import homepage
def SignupPage(request):
    """
    đăng kí tài khoản
    """
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('repassword')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect(views.loginpage)


    return render (request,'home/register.html')
#############################

#Dang nhap tai khoan
def loginpage(request):
    """
    Đăng nhập
    """
    if request.method == 'POST':
        uname = request.POST.get('username')
        paswrd = request.POST.get('password')
        user = authenticate(request, username=uname, password=paswrd)
        print (user.username, user.password)
        if user is not None:
            login(request,user)
            return redirect(homepage.views.index)
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'home/login.html')
#################################

#dang xuat
def LogoutPage(request):
    """
    đăng xuất
    """
    logout(request)
    return redirect(views.loginpage)