# Generated by Django 4.2 on 2023-05-22 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.DateTimeField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.aula')),
            ],
        ),
    ]
