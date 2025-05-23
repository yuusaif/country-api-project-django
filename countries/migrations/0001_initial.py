# Generated by Django 5.2 on 2025-05-06 17:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('official_name', models.CharField(max_length=255)),
                ('currencies', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('subregion', models.CharField(max_length=255)),
                ('area', models.FloatField()),
                ('flag_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
