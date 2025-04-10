from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer
from datetime import datetime

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Логируем текущую дату и время
        now = datetime.now()
        logger.info(f"Current date: {now.date()}, Current time: {now.time()}")

        # Фильтруем просроченные бронирования
        expired_bookings = Booking.objects.filter(status="active").filter(
            date__lt=now.date()
        ) | Booking.objects.filter(
            status="active", date=now.date(), end_time__lt=now.time()
        )

        logger.info(f"Expired bookings count before update: {expired_bookings.count()}")

        # Обновляем статус просроченных бронирований
        updated_count = expired_bookings.update(status="expired")
        logger.info(f"Updated {updated_count} bookings to 'expired'")

        # Возвращаем доступные бронирования (в зависимости от пользователя)
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматическое заполнение поля user текущим авторизованным пользователем
        serializer.save(user=self.request.user)
