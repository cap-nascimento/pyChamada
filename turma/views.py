import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Turma,Inscricao
from aula.models import Aula

from .forms import  *

# Create your views here.

@login_required
def index_turmas(request):
    turmas = Turma.objects.filter(responsavel = request.user)
    return render(request, 'turma/index.html', {
        'turmas' : turmas,
        'responsavel' : request.user,
    })

@login_required
def create_turma(request):
    return render(request, 'turma/create.html', {
        'responsavel': request.user,
        'form': TurmaRegistrationForm(),
    })

@login_required
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

@login_required
def detail_turma(request, turma_id):
    aulas = Aula.objects.filter(turma = turma_id)
    return render(request, 'turma/detail.html', {
        'aulas': aulas,
        'turma': Turma.objects.get(pk = turma_id)
    })

@login_required
def register_aluno(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    try:
        inscricao = Inscricao.objects.get(turma=turma, aluno = request.user)
        messages.error(request, "Inscricao Duplicada!")
        return redirect(reverse('home'))
    except:
        inscricao = Inscricao()
        inscricao.turma = turma
        inscricao.aluno = request.user
        inscricao.save()
        messages.success(request,"Inscricao Realizada")
    return redirect(reverse('home'))