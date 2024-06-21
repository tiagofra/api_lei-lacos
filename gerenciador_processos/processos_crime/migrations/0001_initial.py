# Generated by Django 5.0.6 on 2024-05-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('advogado', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.CharField(choices=[('criminal', 'Criminal'), ('trabalhista', 'Trabalhista'), ('legislativo', 'Legislativo'), ('consumidor', 'Consumidor'), ('ambiental', 'Ambiental'), ('digital', 'Digital'), ('empresarial', 'Empresarial'), ('eleitoral', 'Eleitoral')], max_length=50)),
            ],
        ),
    ]