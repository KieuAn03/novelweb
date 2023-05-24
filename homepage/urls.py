from django.urls import path
from. import views

urlpatterns = [
    path("", views.index),
    path("summary/", views.summary, name="summary" )
]
