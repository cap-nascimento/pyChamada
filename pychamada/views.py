from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm

from django.contrib.auth.models import User

def register(request):
    return render(request, 'registration/register.html', {
        'form': UserRegistrationForm(),
    })


def register_user(request):
    errors = None
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form)
            return redirect(reverse('login'))
        else:
            errors = form.errors.as_json()
        
    return redirect(reverse('register'), {
        'form': UserRegistrationForm(),
        'errors': errors,
    })
