from django.contrib import admin

from .models import Turma, Inscricao


class TurmaAdmin(admin.ModelAdmin):
    fields = [ "codigo", "nome", "responsavel" ]

class InscricaoAdmin(admin.ModelAdmin):
    fields = ["aluno", "turma"]


admin.site.register(Turma, TurmaAdmin)
admin.site.register(Inscricao, InscricaoAdmin)