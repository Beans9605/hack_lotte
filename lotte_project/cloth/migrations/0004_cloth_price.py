# Generated by Django 3.1.2 on 2020-10-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0003_viewofuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]