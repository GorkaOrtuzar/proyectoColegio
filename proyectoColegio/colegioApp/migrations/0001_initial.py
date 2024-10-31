# Generated by Django 4.2.16 on 2024-10-31 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cif', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('antiguedad', models.PositiveIntegerField()),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesores', to='colegioApp.colegio')),
            ],
        ),
    ]
