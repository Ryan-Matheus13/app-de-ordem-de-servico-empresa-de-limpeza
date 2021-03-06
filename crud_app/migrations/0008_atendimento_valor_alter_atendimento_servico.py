# Generated by Django 4.0.3 on 2022-04-10 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0007_alter_atendimento_desconto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.servico'),
        ),
    ]
