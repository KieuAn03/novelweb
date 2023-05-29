from django.urls import path
from. import views
import registerr.views as rg

urlpatterns = [
    path("", views.index, name='homepage'),
    path("dental/", views.deltail, name="deltal" ),
    path("logout/", rg.LogoutPage, name="logout"),
<<<<<<< HEAD
    path("doc/", views.doc, name="doc"),    
    path("comment/", views.add_comment, name="comment"),
=======
    path("doc/", views.doc, name="doc"),
    path("search/", views.search, name="search"),
>>>>>>> c6b8b5eb067ae235b34506223ebbbca7bb99ad08
]
 