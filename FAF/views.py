from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
def home(request):
    courses = Courses.objects.all()
    speeches = Speech.objects.all()
    return render(request,"index.html",{'courses':courses,'speeches':speeches})
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repass = request.POST["repassword"]
        if password == repass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"You username is avaialbe here")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"You email is avaialbe here")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                customer = Customer.objects.create(name=username)
                customer.save()
                return redirect('/login')

        else:
            messages.info(request,"Your passwords are not same")
            return redirect('register')
    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Your data is wrong")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


def course(request):
    main_course = MainCourse.objects.all()
    return render(request,"courses.html",{'courses':main_course})
@login_required(login_url='/login')
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'registration.html', {'form': form})

def about(request):
    return render(request,'about.html')