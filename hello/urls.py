from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nithes",views.nithes,name="nithes"),
    path("<str:name>", views.greet, name="greet"),
]