# Generated by Django 3.0.3 on 2020-03-16 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(blank=True, max_length=50, verbose_name='プラン名')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'Plan',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, max_length=50, verbose_name='タスク名')),
                ('datetime', models.DateTimeField(verbose_name='日時')),
                ('url', models.URLField(null=True, verbose_name='URL')),
                ('task_memo', models.TextField(blank=True, null=True, verbose_name='タスクメモ')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Plan', verbose_name='プラン')),
            ],
            options={
                'verbose_name_plural': 'Task',
            },
        ),
    ]
