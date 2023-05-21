from django.contrib import admin

from .models import Turma


class TurmaAdmin(admin.ModelAdmin):
    fields = [ "codigo", "nome", "responsavel" ]


admin.site.register(Turma, TurmaAdmin)