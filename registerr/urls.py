from django.urls import path
from. import views
import homepage
urlpatterns = [
    path("", homepage.views.index),
    path("login/", views.loginpage, name="login"),
    path("signup/", views.SignupPage, name="signup"),

]
