# Generated by Django 4.1.1 on 2022-12-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transalation',
            name='text',
            field=models.JSONField(blank=True, null=True),
        ),
    ]