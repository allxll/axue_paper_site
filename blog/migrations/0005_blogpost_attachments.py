# Generated by Django 3.1.5 on 2021-02-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210210_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='attachments',
            field=models.ManyToManyField(related_name='references', to='blog.Paper'),
        ),
    ]
