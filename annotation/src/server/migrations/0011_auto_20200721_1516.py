# Generated by Django 2.1.7 on 2020-07-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20200615_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='active',
            new_name='active_learning_strategy',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='embedding',
            new_name='encoding_strategy',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='onlinelearning',
            new_name='is_online_on',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='nounchunk',
            new_name='noun_chunk',
        ),
        migrations.AddField(
            model_name='setting',
            name='model_backed_recs',
            field=models.BooleanField(default=False),
        ),
    ]
