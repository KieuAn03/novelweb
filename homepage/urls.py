from django.urls import path
from. import views
import registerr.views as rg

urlpatterns = [
    path("", views.index, name='homepage'),
    path("deltal/", views.deltail, name="deltal" ),
    path("logout/", rg.LogoutPage, name="logout"),
    path("doc/", views.doc, name="doc"),    
    path("comment/", views.add_comment, name="comment"),
<<<<<<< HEAD
=======
    path("doc/", views.doc, name="doc"),
    path("search/", views.search, name="search"),
>>>>>>> c6b8b5eb067ae235b34506223ebbbca7bb99ad08
=======
    path("delete-comment/", views.delete_comment, name="delete-comment"),
    path("like_truyen/", views.likeTruyen, name="like_truyen"),
    path("favorite/", views.truyenFavo, name="favorite"),

    path("doc/", views.doc, name="doc"),
    path("search/", views.search, name="search"),
<<<<<<< HEAD
=======
>>>>>>> origin/main
>>>>>>> TD
>>>>>>> main
]
 