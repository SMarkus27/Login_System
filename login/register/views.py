from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginUserForm



def login_user(request):
    form = LoginUserForm()
    context = {
        'form':form,
    }
    return render(request,'login.html',context)

# authenticated the user
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request,user)
            return redirect('sucess')    
        else:
            messages.error(request, 'username or password is wrong')
            return redirect('/')        


def logout_user(request):
    logout(request)
    return redirect('login')

# create a new user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        form = CustomUserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'register.html',context)

# only show the sucess, if the user is autheticated
@login_required(login_url='/')
def success(request):
    return render(request,'sucess.html')