from django import forms
from django.core.exceptions import ValidationError

from .models import Turma,Aula,Presenca

class TurmaRegistrationForm(forms.ModelForm):
    # codigo = forms.CharField(label="Nome", max_length=200, required=True)
    # nome = forms.CharField(label="Nome", max_length=200, required=True)
    class Meta:
        model = Turma
        fields = ["codigo", "nome"]

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class AulaRegistrationForm(forms.Form):
    DAYS_OF_WEEK = (
        (0, 'Segunda'),
        (1, 'Terca'),
        (2, 'Quarta'),
        (3, 'Quinta'),
        (4, 'Sexta'),
        (5, 'Sabado'),
        (6, 'Domingo'),
    )

    inicio = forms.TimeField(required=True, widget=TimeInput())
    fim = forms.TimeField(required=True, widget=TimeInput())
    data_inicio = forms.DateField(required=True, widget=DateInput())
    data_final = forms.DateField(required=True, widget=DateInput())
    dias_da_semana = forms.CharField(required=True, widget=forms.CheckboxSelectMultiple(choices=DAYS_OF_WEEK))

    def clean(self):
        inicio = self.cleaned_data['inicio']
        fim = self.cleaned_data['fim']
        data_inicio = self.cleaned_data['data_inicio']
        data_fim = self.cleaned_data['data_final']

        if fim < inicio:
            raise ValidationError("Horario da aula nao pode começar depois de acabar!")
        if data_fim < data_inicio:
            raise ValidationError("Data de inicio das aulas nao pode ser depois do fim!")
