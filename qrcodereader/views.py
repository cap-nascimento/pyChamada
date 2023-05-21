from django.shortcuts import render, redirect
from django.urls import reverse

from turma.models import Turma
from aula.models import Aula

from .utils import generate_qrcode


def qrcode_turma(request, filename):
    return render(request, 'qrcodereader/index.html', {
        'qr_type': 'turma',
        'filename': '/images/' + filename,
    })


def qrcode_presenca(request, filename):
    return render(request, 'qrcodereader/index.html', {
        'qr_type': 'presenca',
    })
    

def qrcode_generator(request, type, id):
    turma = None
    aula = None
    if type == 'turma':
        try:
            turma = Turma.objects.get(id = id)
            return qrcode_generator_helper(request, type, turma)
        except:
            pass
        
    if type == 'aula':
        try:
            aula = Aula.objects.get(id = id)
            return qrcode_generator_helper(request, type, aula)
        except:
            pass
    
    return redirect('home')
    
    
def qrcode_generator_helper(request, type, instance):
    if type == 'turma':
        if instance:
            token = generate_qrcode({
                'url': 'http://localhost:8000/',
                'id': str(instance.id) + '/',
                'codigo': instance.codigo,
            })
            return qrcode_turma(request, token)
        
    if type == 'aula':
        if instance:
            token = generate_qrcode({})
            return qrcode_presenca(request, token)
        