# Generated by Django 4.1.7 on 2023-02-23 02:05

import ImageUploadApi.storage
from django.db import migrations, models
import images.utils
import images.validators


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0003_alter_expiringlink_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expiringlink",
            name="link",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(
                max_length=255,
                storage=ImageUploadApi.storage.GoogleCloudMediaFileStorage,
                upload_to=images.utils.image_upload_path,
                validators=[images.validators.validate_image_extension],
            ),
        ),
    ]
