from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'accounts/main.html')

def user(request):
    students = Student.objects.all()
    total_students = students.count()
    fees_pending = students.filter(fees_status='Pending').count()
    fees_paid = students.filter(fees_status='Paid').count()
    
    context = {
        'students' : students,
        'total_students' : total_students,
        'fees_pending' : fees_pending,
        'fees_paid' : fees_paid
    }
    
    return render(request, 'accounts/dashboard.html', context)

def profile(request, pk_test):
    student = Student.objects.get(id=pk_test)
    context = {
        'student' : student,
    }
    return render(request, 'accounts/profile.html', context)
