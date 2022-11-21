from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<marquee><h2>this is my first project</h2></marquee>')