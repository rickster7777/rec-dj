# Generated by Django 2.2.5 on 2020-03-02 13:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0012_college'),
        ('players', '0066_auto_20200212_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbsSchools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('old', 'old'), ('new', 'new')], default='old', max_length=20)),
                ('fbs_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.FbsOffers')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.School')),
            ],
        ),
    ]