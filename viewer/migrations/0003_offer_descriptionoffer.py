# Generated by Django 4.1.1 on 2024-12-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_rename_description_offer_nameoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='descriptionoffer',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]