# Generated by Django 5.0.4 on 2024-05-18 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='menu',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard.menu', verbose_name='منو'),
        ),
    ]
