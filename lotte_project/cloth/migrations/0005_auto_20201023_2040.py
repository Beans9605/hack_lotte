# Generated by Django 3.1.2 on 2020-10-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0004_cloth_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewofuser',
            name='product',
        ),
        migrations.AddField(
            model_name='viewofuser',
            name='product',
            field=models.ManyToManyField(to='cloth.Cloth'),
        ),
    ]