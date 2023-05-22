from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    matricula = models.CharField(max_length=100)
