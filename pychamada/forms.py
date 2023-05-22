from django import forms
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100, required=True)
    email = forms.EmailField(label="E-mail", max_length=100, required=True)
    matricula = forms.CharField(label="Matrícula", max_length=50, required=True)
    tipo_usuario = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ("PROFESSOR", "Professor"),
            ("ALUNO", "Aluno"),
        ]
    )
    senha = forms.CharField(label="Senha", max_length=20, widget=forms.PasswordInput, required=True) 
    senha_confirmacao = forms.CharField(
        label="Confirme a Senha", max_length=20,
        widget=forms.PasswordInput, required=True
    )
    
    
    def clean(self):
        senha1 = self.cleaned_data['senha']
        senha2 = self.cleaned_data['senha_confirmacao']
        
        if senha1 and senha2:
            if senha1 != senha2:
                raise ValidationError("Passwords must be equal!")
