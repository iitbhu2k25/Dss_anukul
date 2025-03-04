# Generated by Django 5.1.6 on 2025-03-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PDFDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("file", models.FileField(upload_to="pdfs/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "confident_pdfdocument",
            },
        ),
    ]
