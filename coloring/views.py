from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'coloring/index.html')

def start_screen(request):
    return render(request, 'coloring/start_screen.html')

def animals(request):
    return render(request, 'coloring/animals.html')

def flowers(request):
    return render(request, 'coloring/flowers.html')

def landscapes(request):
    return render(request, 'coloring/landscapes.html')
