# Generated by Django 3.1.4 on 2022-06-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcserver', '0002_auto_20220623_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='device_id',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
