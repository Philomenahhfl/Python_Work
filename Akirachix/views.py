from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from.models import datetime

# Create your views here.

def welcome(request):
    return render(request,'welcome_students.html')
def Students(request):
    students = Student.objects.all()
    context = {
        'student':students
    }
    return render(request, 'listing_data.html',context)