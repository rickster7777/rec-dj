# Generated by Django 2.2.5 on 2020-01-22 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0058_fbsdecommit'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbsoffers',
            name='decommit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.FbsDeCommit'),
        ),
    ]