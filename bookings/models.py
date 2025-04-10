from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User


class Booking(models.Model):
    STATUS_CHOICES = [
        ("active", "Активное"),
        ("expired", "Просроченное"),
        ("cancelled", "Отменено"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
