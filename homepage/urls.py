from django.urls import path
from. import views
import registerr.views as rg

urlpatterns = [
    path("", views.index, name='homepage'),
    path("deltal/", views.deltail, name="deltal" ),
    path("logout/", rg.LogoutPage, name="logout"),
    path("doc/", views.doc, name="doc"),    
    path("comment/", views.add_comment, name="comment"),
    path("doc/", views.doc, name="doc"),
    path("search/", views.search, name="search"),
    path("delete-comment/<int:id>/", views.delete_comment, name="delete-comment"),
    path("like_truyen/", views.likeTruyen, name="like_truyen"),
    path("favorite/", views.truyenFavo, name="favorite"),
    path("doc/", views.doc, name="doc"),
    path("search/", views.search, name="search"),
    path("delete-favo", views.delete_favo, name="delete-favo"),
]
 