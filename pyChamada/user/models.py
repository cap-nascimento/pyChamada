from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.IntegerField(primary_key=True)
    cpf = models.IntegerField()
    email = models.EmailField()




class Turma(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    responsavel = models.ForeignKey(User)
    alunos = models.ManyToManyRel(User)



class Aula(models.Model):
    turma = models.ForeignKey(Turma)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()



class Presnca(models.Model):
    aula = models.ForeignKey(Aula)
    aluno = models.ForeignKey(User)
    registro = models.DateTimeField
