# Generated by Django 3.1.5 on 2021-02-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.DateField(blank=True, null=True, verbose_name='Published Year'),
        ),
    ]
