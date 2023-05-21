from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .models import Turma,Aula,Presenca
from .forms import  *

# Create your views here.

def index_turmas(request):
    turmas = Turma.objects.filter(responsavel = request.user)
    template = loader.get_template('turma/index.html')
    context = {
        'turmas' : turmas,
        'responsavel' : request.user,
    }
    return HttpResponse(template.render(context,request))



def create_turma(request):
    template = loader.get_template('turma/create.html')
    context = {
        'responsavel': request.user,
        'form': TurmaRegistrationForm(),
    }
    return HttpResponse(template.render(context, request))

def create_turma_post(request):
    errors = None
    if request.method == 'POST':
        form = TurmaRegistrationForm(request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.responsavel = request.user
            turma.save()
            return redirect(f'/turmas/detail/{turma.pk}')
        else:
            errors = form.errors.as_json()
    else:
        return redirect(reverse('create_turma'), {
            'responsavel': request.user,
            'form': TurmaRegistrationForm(),
            'errors': errors,
        })

def detail_turma(request, turma_id):
    aulas = Aula.objects.filter(turma = turma_id)
    template = loader.get_template('turma/detail.html')
    context = {
        'aulas': aulas,
        'turma': Turma.objects.get(pk = turma_id)
    }
    return HttpResponse(template.render(context, request))
