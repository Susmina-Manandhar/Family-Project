# Generated by Django 3.2.15 on 2022-08-08 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0004_auto_20220808_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profession',
            old_name='profession',
            new_name='professions',
        ),
    ]
