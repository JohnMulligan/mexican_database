# Generated by Django 4.2.8 on 2023-12-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_alter_archivo_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre de Archivo'),
        ),
        migrations.AlterField(
            model_name='fondo',
            name='fondo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='subfondo',
            name='subfondo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='volumen',
            name='volumen',
            field=models.CharField(max_length=150),
        ),
    ]
