from urllib import request
from django.shortcuts import render, HttpResponse

# Create your views here.
html_base= """
<h1> Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de...</a></li>
    <li><a href="/contactos/">contactos</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
</ul>
"""
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contactos(request):
    return render(request, "core/contactos.html")

