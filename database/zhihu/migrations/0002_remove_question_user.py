# Generated by Django 4.1.7 on 2023-02-28 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zhihu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="user",
        ),
    ]