from django.urls import path

from . import views


urlpatterns = [
    path('<int:turma_id>/create/aula', views.create_aula, name='create_aula'),
    path('<int:turma_id>/create/aula/post', views.create_aula_post, name='create_aula_post'),
]