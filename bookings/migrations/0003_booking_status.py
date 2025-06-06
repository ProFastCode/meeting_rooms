# Generated by Django 4.2 on 2025-04-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0002_alter_booking_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "Активное"),
                    ("expired", "Просроченное"),
                    ("cancelled", "Отменено"),
                ],
                default="active",
                max_length=20,
            ),
        ),
    ]
