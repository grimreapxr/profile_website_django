from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def register(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')    
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def homePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'home.html', context)

@login_required
def profilePage(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login
    }
    return render(request,'profile.html',context)

class ChangePasswordPage(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')