from django.urls import path
from . import views

urlpatterns = [
    path("", views.salom, name='index'),
    path("maktab/", views.maktabView, name='maktab'),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("login/praktika/", views.praktika, name='praktika'),
    path("logout/",views.logout,name='logout')
]
