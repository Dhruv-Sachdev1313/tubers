# Generated by Django 3.2.9 on 2021-12-04 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
