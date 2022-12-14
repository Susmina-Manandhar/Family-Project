# Generated by Django 3.2.15 on 2022-08-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0005_rename_profession_profession_professions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overall',
            name='professionlist',
        ),
        migrations.AddField(
            model_name='overall',
            name='project',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profession',
            name='namelist',
            field=models.OneToOneField(default='Add', on_delete=django.db.models.deletion.CASCADE, to='Members.information'),
        ),
        migrations.AlterField(
            model_name='overall',
            name='namelist',
            field=models.OneToOneField(default='Add', on_delete=django.db.models.deletion.CASCADE, to='Members.information'),
        ),
    ]
