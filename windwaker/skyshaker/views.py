from django.shortcuts import render
from skyshaker.models import Tag

def index(request):
    return render(request, 'skyshaker/index.html')

def donate(request):
    return render(request, 'skyshaker/donate.html')
