# Generated by Django 3.2.15 on 2022-08-08 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0006_auto_20220808_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overall',
            name='namelist',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='Members.information'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='namelist',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='Members.information'),
        ),
    ]