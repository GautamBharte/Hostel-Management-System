from cmath import log
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import StudentForm, CreateUserForm
from .filters import StudentFilter

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else: 
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'accounts/main.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def profile(request, pk_test):
    student = Student.objects.get(id=pk_test)
    context = {
        'student' : student,
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('/user')
    context ={
        'student' : student
    }
    return render(request, 'accounts/delete_student.html', context)