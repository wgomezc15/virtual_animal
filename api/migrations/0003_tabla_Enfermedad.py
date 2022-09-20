# Generated by Django 4.1 on 2022-09-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_typedocument_options_alter_typedocument_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabla_Enfermedad',
            fields=[
                ('id_Enfermedad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Enfermedad', models.TextField(max_length=20, unique=True, verbose_name='Enfermedad')),
                ('Descripcion_Enfermedad', models.TextField(max_length=200, unique=True, verbose_name='Descripciondeenfermedad')),
            ],
        ),
    ]