# Generated by Django 4.0.4 on 2022-05-07 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlfitos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variedad',
            name='cultivo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cultivo_name', to='controlfitos.cultivo'),
        ),
    ]
