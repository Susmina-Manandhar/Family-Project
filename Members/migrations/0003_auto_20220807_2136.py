# Generated by Django 3.2.15 on 2022-08-07 15:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0002_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='profession',
        ),
        migrations.AddField(
            model_name='profession',
            name='namelist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='namelist', to='Members.information'),
        ),
        migrations.AddField(
            model_name='profession',
            name='professionlist',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='professionlist', to='Members.information'),
            preserve_default=False,
        ),
    ]
