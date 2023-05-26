from django.urls import path
from. import views
import registerr.views as rg
urlpatterns = [
    path("", views.index),
    path("summary/", views.deltail, name="deltal" ),
    path("logout/", rg.LogoutPage, name="logout")
]
