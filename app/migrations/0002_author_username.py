# Generated by Django 5.0.2 on 2024-02-28 20:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=28),
            preserve_default=False,
        ),
    ]
