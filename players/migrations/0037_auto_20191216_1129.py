# Generated by Django 2.2.5 on 2022-12-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0036_auto_20221212_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]