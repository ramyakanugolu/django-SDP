from django.contrib import messages
from django.contrib.auth.models import *
from django.shortcuts import render, redirect
from .models import LeaveRequest
from .forms import LeaveRequestForm, LeaveForm
from django import forms


def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})

def create_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_request_list')  # Redirect to leave request list after submission
    else:
        form = LeaveRequestForm()
    return render(request, 'create_leave_request.html', {'form': form})


def home(request):
    return render(request,'homepage.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None :
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

'''def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                        password=password1)

        user.save()
        return redirect(request,'login.html')
    return render(request,"signup.html")'''



def user_signup(request):
 if request.method=="POST":
     username=request.POST['username']
     pass1=request.POST['password1']
     pass2=request.POST['password2']
     if pass1==pass2:
         if User.objects.filter(username=username).exists():
             messages.info(request,'OOPs! Username already taken')
             return render(request,'signup.html')
         else:
             user = User.objects.create_user(username=username, password=pass1)
             user.save()
             messages.info(request,'Account created successfully')
             return render(request,'login.html')
 else :
     return render(request,'signup.html')



def home_view(request):
    return render(request, 'homepage.html')
def newhomepage(request):
    return render(request, 'newhomepage.html')

def logout(request):
    auth.logout(request)
    return render(request,'homepage.html')

def leave_request(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            # Process form data
            leave_date = form.cleaned_data['leave_date']
            # Perform further actions
    else:
        form = LeaveForm()
    return render(request, 'leave_request.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.core.mail import send_mail
from django.conf import settings


def user_signup(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            role = form.cleaned_data['role']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken')
                    return render(request, 'signup.html', {'form': form})
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    # Set the user's role
                    user.role = role
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')  # Redirect to login page
            else:
                messages.error(request, 'Passwords do not match')
                return render(request, 'signup.html', {'form': form})
    else:
        form = EmployeeForm()

    return render(request, 'signup.html', {'form': form})