# Generated by Django 4.1.7 on 2023-02-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zhihu", "0005_answer_comment_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(db_index=True, max_length=16),
        ),
    ]
