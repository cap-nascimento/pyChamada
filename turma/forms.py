from django import forms
from django.core.exceptions import ValidationError

from .models import Turma

class TurmaRegistrationForm(forms.ModelForm):
    # codigo = forms.CharField(label="Nome", max_length=200, required=True)
    # nome = forms.CharField(label="Nome", max_length=200, required=True)
    class Meta:
        model = Turma
        fields = ["codigo", "nome"]