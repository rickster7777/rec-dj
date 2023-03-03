# Generated by Django 2.2.5 on 2020-02-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0063_remove_notes_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='note_comments', to='players.Comments'),
        ),
    ]