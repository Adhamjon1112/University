# Generated by Django 5.0.3 on 2024-10-05 11:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0005_alter_student_id_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="images/profile_image.png",
                null=True,
                upload_to="images/",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
