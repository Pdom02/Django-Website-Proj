# Generated by Django 4.2 on 2023-05-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_listing_sellerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
