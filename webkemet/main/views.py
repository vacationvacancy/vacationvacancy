
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import UserRegistrationForm
from django.db import models
from .models import Figure


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/contact.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')


def figures_view(request):
    figures = Figure.objects.all()
    return render(request, 'figures.html', {'figures': figures})