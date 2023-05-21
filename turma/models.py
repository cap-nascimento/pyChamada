from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Turma(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    # alunos = models.ManyToManyRel(User)
    