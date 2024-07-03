from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

def registerpage(request):
    form = CreateUserForm()
    if request.method == 'GET':
        return render(request,'register.html',{'form': form})
    
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'You have signed up {username}')
            return redirect('login')
        else:
            return render(request,'register.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,' Username or password is incorrect')
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