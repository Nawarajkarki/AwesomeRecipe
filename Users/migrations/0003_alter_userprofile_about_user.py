# Generated by Django 4.2.5 on 2023-10-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0002_user_is_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="about_user",
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
