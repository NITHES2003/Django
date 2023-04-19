from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, Nithes")

def nithes(request):
    return HttpResponse("Hello, Nithes!!!!")

def greet(request,name):
    return HttpResponse(f"Good Morning {name.capitalize()}")
