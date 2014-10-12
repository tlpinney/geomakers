from django.shortcuts import render, get_object_or_404
from skyshaker.models import Project, Tag
from django.conf import settings

def index(request):
    return render(request, 'skyshaker/index.html')

def donate(request):
    return render(request, 'skyshaker/donate.html')

def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'skyshaker/project.html', {'project': project})
