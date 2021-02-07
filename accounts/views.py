from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

# Create your views here.
from django.urls import reverse_lazy

from accounts.forms import UserProfileForm, LoginForm
from accounts.models import UserProfile
from cars.models import Car


@transaction.atomic
def register(req):
    if req.user.is_authenticated:
        return redirect('index')
    if req.method == 'GET':

        context = {
            'form': UserCreationForm,
            'profile_form': UserProfileForm,
        }
        return render(req, 'register.html', context)
    elif req.method == 'POST':
        user_form = UserCreationForm(req.POST)
        profile_form = UserProfileForm(req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(req, user)
            return redirect('index')
        context = {
            'form': user_form,
            'profile_form': profile_form,
        }
        return render(req, 'register.html', context)


class LogoutUserView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


# class LoginUserView(auth_views.LoginView):
#     template_name = 'login.html'


def login_user(req):
    if req.user.is_authenticated:
        return redirect('index')
    if req.method == 'GET':
        context = {
            'form': LoginForm()
        }
        return render(req, 'login.html', context)
    else:
        login_form = LoginForm(req.POST)
        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('index')

            context = {
                'form': login_form
            }
            return render(req, 'login.html', context)


def show_profile(req, pk):
    user = User.objects.get(pk=pk)
    cars = Car.objects.all()
    cars = [x for x in cars if x.user.user == user]
    if req.user == user:
        return redirect('current profile')
    profile = UserProfile.objects.get(user=user)
    context = {
        'profile': profile,
        'cars': cars
    }
    return render(req, 'profile.html', context)


@login_required
def your_profile(req):
    cars = Car.objects.all()
    cars = [x for x in cars if x.user.user == req.user]
    profile = UserProfile.objects.get(user=req.user)
    context = {
        'profile': profile,
        'cars': cars
    }

    return render(req, 'current_profile.html', context)
