import django_filters
from .models import Room
from bookings.models import Booking
from datetime import datetime


class RoomFilter(django_filters.FilterSet):
    min_capacity = django_filters.NumberFilter(field_name="capacity", lookup_expr="gte")
    floor = django_filters.NumberFilter(field_name="floor")
    date = django_filters.DateFilter(method="filter_by_datetime")
    start_time = django_filters.TimeFilter(method="filter_by_datetime")
    end_time = django_filters.TimeFilter(method="filter_by_datetime")

    class Meta:
        model = Room
        fields = ["floor", "min_capacity", "date", "start_time", "end_time"]

    def filter_by_datetime(self, queryset, name, value):
        # Получаем дату, время начала и окончания из запроса
        date = self.data.get("date")
        start_time = self.data.get("start_time")
        end_time = self.data.get("end_time")

        if date and start_time and end_time:
            # Преобразуем значения в datetime-объекты
            start_datetime = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")

            # Исключаем комнаты, которые заняты в указанный диапазон времени
            return queryset.exclude(
                bookings__date=date,
                bookings__start_time__lt=end_datetime.time(),
                bookings__end_time__gt=start_datetime.time(),
            ).distinct()

        return queryset
