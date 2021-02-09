# Generated by Django 3.1.5 on 2021-02-09 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('date_created', models.DateField(default=datetime.date(2021, 2, 9))),
                ('author', models.CharField(blank=True, max_length=60)),
                ('main_text', models.TextField(blank=True)),
                ('is_hidden', models.BooleanField(default=False)),
            ],
        ),
    ]
