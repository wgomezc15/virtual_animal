from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api',),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_Enfermedades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False))
                ('id_Enfermedad', models.AutoField(primary_key=True, serialize=False)),
                ('name_Enfermedad', models.CharField(max_length=30, verbose_name='Name')),
                ('descripcion_Enfermedad', (models.TextField)),
                ('fecha_creacion' models.DateField('fecha_creacion',auto_now =False, auto_now_add=True))
            ],
        ),
    ]

    
        
       