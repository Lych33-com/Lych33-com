# Generated by Django 4.1.3 on 2022-11-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_remove_user_website"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
