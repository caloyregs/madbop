# Generated by Django 2.2.2 on 2019-08-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_auto_20190819_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
