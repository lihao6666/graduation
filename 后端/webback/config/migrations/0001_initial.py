# Generated by Django 3.0.5 on 2021-04-28 08:06

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigMes',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('parse_type', models.CharField(max_length=20, verbose_name='爬虫类别')),
                ('headers', models.TextField(verbose_name='请求头headers')),
                ('cookies', models.TextField(verbose_name='cookies')),
            ],
            options={
                'verbose_name': '配置信息',
                'db_table': 'Config',
            },
        ),
    ]
