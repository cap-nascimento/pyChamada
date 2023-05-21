from django.contrib import admin

from turma.models import Turma,Aula,Presenca

class TurmaAdmin(admin.ModelAdmin):
    fields = [ "codigo", "nome", "responsavel" ]

class AulaAdmin(admin.ModelAdmin):
    fields = [ "turma", "inicio", "fim" ]

class PresencaAdmin(admin.ModelAdmin):
    fields = [ "aula", "aluno", "registro" ]

# Register your models here.

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Presenca, PresencaAdmin)