# Generated by Django 5.0.6 on 2024-05-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangopress_media", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mediaasset",
            name="file",
            field=models.FileField(default="", upload_to=""),
            preserve_default=False,
        ),
    ]
