from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Subject

# Create your views here.

def course(request):
    courses = Subject.objects.all()
    context = { 'course': courses }
    return render(request, 'subjects/course.html', context)

def apply(request):
    return render(request, 'subjects/apply.html')