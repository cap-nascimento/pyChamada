from django.contrib import admin

from .models import Aula, Presenca


class AulaAdmin(admin.ModelAdmin):
    fields = [ "turma", "inicio", "fim" ]

class PresencaAdmin(admin.ModelAdmin):
    fields = [ "aula", "aluno", "registro" ]


admin.site.register(Aula, AulaAdmin)
admin.site.register(Presenca, PresencaAdmin)