# Generated by Django 4.0.4 on 2022-04-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlfitos', '0007_remove_cliente_cif'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cif',
            field=models.CharField(default='', max_length=10),
        ),
    ]