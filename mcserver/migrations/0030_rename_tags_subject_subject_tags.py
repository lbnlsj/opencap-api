# Generated by Django 4.2 on 2024-02-08 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mcserver", "0029_subject_tags_alter_analysisresult_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subject",
            old_name="tags",
            new_name="subject_tags",
        ),
    ]