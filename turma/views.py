from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Turma,Inscricao
from aula.models import Aula, Presenca
from permissions.models import UserRole

from .forms import  *

from qrcodereader.utils import decrypt_content, format_datetime, timecount

# Create your views here.

@login_required
def index_turmas(request):
    user_role = UserRole.objects.get(user_id = request.user.id)
    turmas = None
    if user_role.role == 'PROFESSOR':
        turmas = Turma.objects.filter(responsavel = request.user)
        
    return render(request, 'turma/index.html', {
        'turmas' : turmas,
        'responsavel' : request.user,
        'user_role': user_role.role
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
    user_role = UserRole.objects.get(user_id = request.user.id)
    return render(request, 'turma/detail.html', {
        'aulas': aulas,
        'turma': Turma.objects.get(pk = turma_id),
        'user_role': user_role.role,
    })


def search_turma(request):
    if request.method == 'POST':
        keyword = request.POST.get('codigo_turma')
        turmas = Turma.objects.filter(string__contains=keyword)
        
    return redirect(reverse('index_turmas'))


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


def register_presenca(request, token):
    message = decrypt_content(token, 'user password')
    register_time, aula_id = message.split(',')
    register_time = datetime.strptime(register_time, '%d-%m-%y %H:%M:%S')
    current_time = format_datetime(datetime.now())
    diff_time = current_time - register_time
    elapsed_time = timecount(str(diff_time))
    if elapsed_time <= 300:
        aula = Aula.objects.get(id = aula_id)
        presenca = Presenca(
            aula = aula, aluno = request.user, registro = register_time
        )
        presenca.save()
        messages.success(request, 'Presença registrada!')
    else:
        messages.error(request, 'Tempo Esgotado!')
        
    return redirect(reverse('home'))