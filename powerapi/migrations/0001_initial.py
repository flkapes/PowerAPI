# Generated by Django 5.1.1 on 2024-09-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CPUModel",
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
                ("cpu_id", models.CharField(max_length=100)),
                ("current_load", models.FloatField()),
                ("estimated_powerdraw", models.FloatField()),
                ("current_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="GPUModel",
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
                ("gpu_id", models.CharField(max_length=100)),
                ("current_load", models.FloatField()),
                ("estimated_powerdraw", models.FloatField()),
                ("current_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="HDDModel",
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
                ("model_number", models.CharField(max_length=10)),
                ("current_io", models.FloatField()),
                ("estimated_powerdraw", models.FloatField()),
                ("current_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
