# Generated by Django 2.1.7 on 2020-06-15 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_label_user_provided'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationextractionannotation',
            old_name='end_offset_2',
            new_name='obj_end_offset',
        ),
        migrations.RenameField(
            model_name='relationextractionannotation',
            old_name='start_offset_2',
            new_name='obj_start_offset',
        ),
        migrations.RenameField(
            model_name='relationextractionannotation',
            old_name='end_offset_1',
            new_name='sbj_end_offset',
        ),
        migrations.RenameField(
            model_name='relationextractionannotation',
            old_name='start_offset_1',
            new_name='sbj_start_offset',
        ),
    ]
