from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import StudentForm, CreateUserForm
from .filters import StudentFilter
from .decorators import *

# Create your views here.
@login_required(login_url='login')
@admin_only
def registerPage(request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
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
    return redirect(home)


def home(request):
    return render(request, 'accounts/main.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentDashboard(request):
    student = request.user.student
    print("STUDENT : ", student)
    context = {
        'student' : student
    }
    return render(request, 'accounts/student_dashboard.html', context)

@login_required(login_url='login')
@admin_only
def user(request):
    students = Student.objects.all()
    total_students = students.count()
    fees_pending = students.filter(fees_status='Pending').count()
    fees_paid = students.filter(fees_status='Paid').count()
    
    print(request.GET)
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
@allowed_users(allowed_roles=['admin'])
def profile(request, pk_test):
    student = Student.objects.get(id=pk_test)
    context = {
        'student' : student,
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addStudent(request):
    
    form = StudentForm()
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # user = User.objects.create_user(StudentForm, StudentForm.email, StudentForm)
            # user.save()
            return redirect('/user')
        
    
    context = {
        'form' : form
    }
    
    return render(request, 'accounts/student_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('/user')
    context ={
        'student' : student
    }
    return render(request, 'accounts/delete_student.html', context)