from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    responsavel = models.ForeignKey(User)
    alunos = models.ManyToManyRel(User)


class Aula(models.Model):
    turma = models.ForeignKey(Turma)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()


class Presenca(models.Model):
    aula = models.ForeignKey(Aula)
    aluno = models.ForeignKey(User)
    registro = models.DateTimeField
