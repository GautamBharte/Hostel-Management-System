from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StudentForm

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

def addStudent(request):
    
    form = StudentForm()
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    
    context = {
        'form' : form
    }
    
    return render(request, 'accounts/add_student.html', context)