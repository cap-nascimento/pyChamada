from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm

from django.contrib.auth.models import User
from permissions.models import UserRole


def register(request):
    errors = []
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.data['nome'], email=form.data['email'], 
                    password=form.data['senha']
                )
                user_role = UserRole(
                    user = user,
                    role = form.data['tipo_usuario'],
                    matricula = form.data['matricula'],
                )
                user_role.save()
                return redirect(reverse('login'))
            except:
                errors.append('An error occurred!')
        else:
            for key in form.errors.keys():
                for value in form.errors[key]:
                    errors.append(value)
        
    return render(request, 'registration/register.html', {
        'form': UserRegistrationForm(),
        'errors': errors,
    })
