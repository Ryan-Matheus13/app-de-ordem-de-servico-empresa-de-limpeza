# Generated by Django 4.0.3 on 2022-04-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0009_rename_valor_atendimento_valor_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
