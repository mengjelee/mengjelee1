# Generated by Django 2.0.6 on 2018-10-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmessage',
            name='talker',
            field=models.CharField(max_length=10),
        ),
    ]
