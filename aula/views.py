from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AulaRegistrationForm

from turma.models import Turma
from .models import Aula

import datetime


def create_aula(request, turma_id):
    return render(request, 'aula/create.html', {
        'turma': Turma.objects.get(pk = turma_id),
        'form': AulaRegistrationForm(),
    })

def create_aula_post(request, turma_id):
    errors = None
    if request.method == 'POST':
        form = AulaRegistrationForm(request.POST)
        if form.is_valid():

            turma = Turma.objects.get(pk=turma_id)
            dias_da_semana = [int(x) for x in form.cleaned_data['dias_da_semana'] if x.isdigit()]
            data = form.cleaned_data['data_inicio']
            data_final = form.cleaned_data['data_final']
            inicio = form.cleaned_data['inicio']
            fim = form.cleaned_data['fim']
            delta = datetime.timedelta(days=1)

            while data <= data_final:
                if data.weekday() in dias_da_semana:
                    aula = Aula()
                    aula.turma = turma
                    aula.inicio = datetime.datetime.combine(data, inicio)
                    aula.fim = datetime.datetime.combine(data, fim)
                    aula.save()
                data += delta

            return redirect(f'/turmas/detail/{turma_id}')
        else:
            errors = form.errors.as_json()
    else:
        return redirect(reverse('create_aula'), {
            'turma': Turma.objects.get(pk = turma_id),
            'form': AulaRegistrationForm(),
            'errors': errors,
        })