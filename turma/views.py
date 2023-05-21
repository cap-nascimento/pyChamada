from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .models import Turma,Aula,Presenca

# Create your views here.

def index_turmas(request, responsavel_id):
    turmas = Turma.objects.filter(responsavel = responsavel_id)
    template = loader.get_template('turma/index.html')
    context = {
        'turmas' : turmas,
        'responsavel_id' : responsavel_id,
    }
    return HttpResponse(template.render(context,request))

