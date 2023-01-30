from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('login', views.ulogin,name="login"),
    path('logout', views.logout,name="logout"),
    path('addcourse', views.addcourse,name="addcourse"),
    path('showcourse', views.showcourse,name="showcourse"),
    path('delete', views.delete,name="delete"),
    path('update', views.update,name="update"),
]
