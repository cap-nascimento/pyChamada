from django.urls import path

from . import views
from aula.views import create_aula, create_aula_post

urlpatterns = [
    # turma paths
    path('', views.index_turmas, name='index_turmas'),
    path('create/turma/', views.create_turma, name='create_turma'),
    path('create/turma/post/', views.create_turma_post, name='create_turma_post'),
    path('detail/<int:turma_id>/', views.detail_turma, name='detail_turma'),
    # path('search/', views.search_turma, name="search_turma"),
    
    # turma - aula paths
    path('<int:turma_id>/create/aula/', create_aula, name='create_aula'),
    path('<int:turma_id>/create/aula/post/', create_aula_post, name='create_aula_post'),
    
    # turma - user / turma - presenca paths
    path('<int:turma_id>/register/', views.register_aluno, name='register_aluno'),
    path('aula/<path:token>/', views.register_presenca, name='register_presenca'),

    path('aluno/frequencia/<int:turma_id>/', views.frequencia_aluno, name='frequencia_aluno'),
    path('frequencia/<int:turma_id>/', views.tabela_alunos, name='frequencia_turma'),
]