# Generated by Django 3.2.9 on 2021-12-27 13:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0014_alter_integration_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='activity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=225), default='', size=None),
        ),
    ]