# Generated by Django 3.0.3 on 2020-03-18 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200317_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificPlanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_book', models.BooleanField(verbose_name='いいねか')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Plan', verbose_name='プラン')),
            ],
        ),
    ]
