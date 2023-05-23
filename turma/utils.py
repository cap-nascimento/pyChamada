import pandas as pd

from .models import Turma,Inscricao
from aula.models import Aula, Presenca
from permissions.models import UserRole

def tabela_frequenica(request, turma_id, alunos=None):
    if alunos is None:
        alunos = [request.user]
    turma = Turma.objects.get(pk = turma_id)
    aulas = Aula.objects.filter(turma= turma)

    rows= []

    for a in alunos:
        matricula = UserRole.objects.get(user = a).matricula
        d = {}
        d['Aluno'] = matricula

        for aula in aulas:
            d[aula.inicio.date()] = False


        presencas = Presenca.objects.filter(aluno = request.user)
        for p in presencas:
            if p.aula in aulas:
                key = p.aula.inicio.date()
                d.key = True
        rows.append(d)

    df = pd.DataFrame(rows)

    return df.to_html(index=False)
