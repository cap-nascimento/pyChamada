from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_turmas, name='index_turmas'),
    path('create/turma/', views.create_turma, name='create_turma'),
    path('create/turma/post/', views.create_turma_post, name='create_turma_post'),
    path('detail/<int:turma_id>/', views.detail_turma, name='detail_turma'),
]