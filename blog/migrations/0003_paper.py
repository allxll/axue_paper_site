# Generated by Django 3.1.5 on 2021-02-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210209_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(blank=True, max_length=60)),
                ('year', models.DateField(blank=True, verbose_name='Published Year')),
                ('attachment', models.FileField(upload_to='papers/')),
            ],
        ),
    ]
