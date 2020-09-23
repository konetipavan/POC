from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def class_room(request):
    return HttpResponse ("Welcome to Class Room Application")
