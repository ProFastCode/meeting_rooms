from rest_framework import serializers
from .models import Booking
from rooms.models import Room


class BookingSerializer(serializers.ModelSerializer):
    # Поле user становится read_only
    user = serializers.ReadOnlyField(source="user.username")
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        # Проверка: Комната уже занята в указанное время
        existing = Booking.objects.filter(
            room=data["room"],
            date=data["date"],
            start_time__lt=data["end_time"],
            end_time__gt=data["start_time"],
        ).exists()

        if existing:
            raise serializers.ValidationError("Комната уже занята в это время")

        # Проверка: Пользователь уже забронировал другую комнату на то же время
        user_bookings = Booking.objects.filter(
            user=self.context["request"].user,
            date=data["date"],
            start_time__lt=data["end_time"],
            end_time__gt=data["start_time"],
        ).exists()

        if user_bookings:
            raise serializers.ValidationError("У вас уже есть бронь на это время")

        return data
