# Generated by Django 4.1.3 on 2022-12-20 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0006_comment"),
    ]

    operations = [
        migrations.DeleteModel(name="Comment",),
    ]
