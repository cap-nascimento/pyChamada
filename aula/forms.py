from django import forms
from django.core.exceptions import ValidationError


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

    inicio = forms.TimeField(required=True, widget=forms.TimeInput())
    fim = forms.TimeField(required=True, widget=forms.TimeInput())
    data_inicio = forms.DateField(required=True, widget=forms.TimeInput())
    data_final = forms.DateField(required=True, widget=forms.TimeInput())
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