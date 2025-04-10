from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rooms.models import Room


class RoomAPITestCase(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Test Room", capacity=10, floor=1)

    def test_get_rooms(self):
        response = self.client.get(reverse("rooms-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
