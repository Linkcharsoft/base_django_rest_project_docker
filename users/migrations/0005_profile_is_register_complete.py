# Generated by Django 5.1 on 2024-09-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_tokenrecovery_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_register_complete",
            field=models.BooleanField(default=False),
        ),
    ]