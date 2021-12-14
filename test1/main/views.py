from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")


def europe_window(request):
    return render(request, "main/Europe.html")


def ukraine_window(request):
    return render(request, "main/Ukraine.html")


def asia_window(request):
    return render(request, "main/Asia.html")