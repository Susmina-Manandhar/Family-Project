# Generated by Django 3.2.15 on 2022-08-08 02:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0003_auto_20220807_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='namelist',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='professionlist',
        ),
        migrations.AddField(
            model_name='profession',
            name='profession',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='overall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='namelist', to='Members.information')),
                ('professionlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.profession')),
            ],
        ),
    ]
