from django.urls import path

from . import views


urlpatterns = [
    path('generator/<str:type>/<int:id>', views.qrcode_generator, name='qrcode_generator'),
    path('turma/<str:token>', views.qrcode_turma, name='qrcode_turma'),
    path('presenca/<str:token>', views.qrcode_presenca, name='qrcode_presenca'),
]
