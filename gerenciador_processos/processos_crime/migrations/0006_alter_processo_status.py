# Generated by Django 5.0.6 on 2024-05-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos_crime', '0005_processo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='status',
            field=models.CharField(choices=[('aberto', 'Aberto'), ('fechado', 'Fechado'), ('arquivado', 'Arquivado')], default='aberto', max_length=100),
        ),
    ]
