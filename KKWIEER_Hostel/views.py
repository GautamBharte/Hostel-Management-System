from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StudentForm
from .filters import StudentFilter

# Create your views here.
def home(request):
    return render(request, 'accounts/main.html')

def user(request):
    students = Student.objects.all()
    total_students = students.count()
    fees_pending = students.filter(fees_status='Pending').count()
    fees_paid = students.filter(fees_status='Paid').count()
    
    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs
    
    context = {
        'students' : students,
        'total_students' : total_students,
        'fees_pending' : fees_pending,
        'fees_paid' : fees_paid,
        'myFilter' : myFilter
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
    
    return render(request, 'accounts/student_form.html', context)

def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/user')
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/student_form.html', context)

def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('/user')
    context ={
        'student' : student
    }
    return render(request, 'accounts/delete_student.html', context)