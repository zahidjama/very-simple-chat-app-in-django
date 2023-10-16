from django.urls import path
from . import views
urlpatterns=[
    path("signin", views.signin, name="signin"),
    path("login", views.login_user, name="login"),
    path("home", views.home_page, name="home"),
    path("chat", views.chat, name="chat"),
    path("", views.index, name="index")
]