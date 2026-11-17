from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, 'Please fill in all fields.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')

        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            messages.success(request, 'Account created successfully!')
            return redirect('register')

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('task_list')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
