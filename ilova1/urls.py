from django.urls import path
from . import views

urlpatterns = [
    path("salom/", views.salom)
]
