from django.urls import path
from. import views
import registerr.views as rg
urlpatterns = [
    path("", views.index),
    path("dental/", views.deltail, name="deltal" ),
    path("logout/", rg.LogoutPage, name="logout"),
    path("doc/", views.doc, name="doc"),    
    path("comment/", views.cmt, name="comment"),
]
 