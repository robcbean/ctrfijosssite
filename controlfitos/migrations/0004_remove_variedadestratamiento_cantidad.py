# Generated by Django 4.0.4 on 2022-05-07 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlfitos', '0003_alter_variedad_cultivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variedadestratamiento',
            name='cantidad',
        ),
    ]