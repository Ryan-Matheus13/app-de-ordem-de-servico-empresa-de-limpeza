# Generated by Django 4.0.3 on 2022-04-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_do_servico', models.DateTimeField()),
                ('situacao', models.CharField(choices=[('Em andamento', 'Em andamento'), ('Concluido', 'Concluido'), ('Cancelado', 'Cancelado')], max_length=12)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11)),
                ('data_de_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=11)),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=4)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_servico', models.CharField(max_length=60)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
