# Generated by Django 5.1.4 on 2024-12-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.IntegerField(max_length=1000),
        ),
    ]
