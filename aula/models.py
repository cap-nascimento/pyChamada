from django.db import models

from django.contrib.auth.models import User
from turma.models import Turma


class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    
    
class Presenca(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    registro = models.DateTimeField()