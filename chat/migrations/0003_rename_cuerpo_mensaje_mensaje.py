# Generated by Django 4.2.7 on 2023-11-18 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_mensaje_fecha_creacion_alter_mensaje_cuerpo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='cuerpo',
            new_name='mensaje',
        ),
    ]
