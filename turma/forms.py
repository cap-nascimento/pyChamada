from django import forms
from .models import Turma,Aula,Presenca

class TurmaRegistrationForm(forms.ModelForm):
    # codigo = forms.CharField(label="Nome", max_length=200, required=True)
    # nome = forms.CharField(label="Nome", max_length=200, required=True)
    class Meta:
        model = Turma
        fields = ["codigo", "nome"]
