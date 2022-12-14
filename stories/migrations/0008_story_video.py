# Generated by Django 4.1.3 on 2023-01-04 11:00

from django.db import migrations, models
import stories.validators


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0007_delete_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="story",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="videos",
                validators=[stories.validators.validate_file_extension],
            ),
        ),
    ]
