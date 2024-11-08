# Generated by Django 3.1.4 on 2022-06-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='device_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='status',
            field=models.CharField(default='recording', max_length=64),
        ),
        migrations.AlterField(
            model_name='video',
            name='device_id',
            field=models.UUIDField(),
        ),
    ]