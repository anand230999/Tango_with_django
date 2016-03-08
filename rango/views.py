from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there world! <a href="+"/rango/about"+">About</a> <html>")
def about(request):
    return HttpResponse("<html> Rango says here is the about page. <a href="+"/rango/"+"> Home </a> <html>")
