# Generated by Django 3.0.7 on 2021-02-21 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20210221_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='origin',
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
