from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

router = DefaultRouter()
router.register("rooms", RoomViewSet, basename="rooms")

urlpatterns = [
    path("", include(router.urls)),
]
