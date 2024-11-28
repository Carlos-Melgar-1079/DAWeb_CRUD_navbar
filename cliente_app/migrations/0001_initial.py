# Generated by Django 5.1.3 on 2024-11-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido_materno', models.CharField(max_length=45)),
                ('apellido_paterno', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]