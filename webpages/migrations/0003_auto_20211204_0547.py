# Generated by Django 3.2.9 on 2021-12-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_auto_20210207_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]