# Generated by Django 3.0.3 on 2020-03-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
