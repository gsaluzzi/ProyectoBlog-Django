# Generated by Django 4.2.7 on 2023-11-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_cuerpo_mensaje_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=models.CharField(max_length=200),
        ),
    ]
