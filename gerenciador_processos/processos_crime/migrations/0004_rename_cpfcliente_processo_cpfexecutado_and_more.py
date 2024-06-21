# Generated by Django 5.0.6 on 2024-05-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos_crime', '0003_rename_descricao_processo_descricaocaso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processo',
            old_name='cpfCliente',
            new_name='cpfExecutado',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='nomeAdvogado',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='nomeCliente',
        ),
        migrations.AddField(
            model_name='processo',
            name='advogadoExecutado',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='advogadoExequente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='cpfExequente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='local',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='natureza',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='nomeExecutado',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='nomeExequente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='oabAdvExecutado',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='oabAdvExequente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='processo',
            name='poderJudiciario',
            field=models.CharField(default='', max_length=100),
        ),
    ]
