# Generated by Django 4.2.1 on 2023-05-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metadata", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="description",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="department",
            old_name="description",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="location",
            old_name="description",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="subcategory",
            old_name="description",
            new_name="name",
        ),
        migrations.AddField(
            model_name="sku",
            name="sku",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
