# Generated by Django 3.0.5 on 2021-05-04 01:55

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0003_auto_20210502_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchItem',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('search_content', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('patch', models.IntegerField()),
            ],
            options={
                'db_table': 'Search',
            },
        ),
    ]
