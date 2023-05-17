from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
