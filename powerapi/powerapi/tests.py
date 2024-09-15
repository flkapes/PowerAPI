from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import HDDModel, CPUModel 

class HDDAPITests(APITestCase):
    def setUp(self):
        self.hdd = HDDModel.objects.create(model_number="HUH721212ALE622", disk_uuid="268b-a342-9037-33a0c848a2e4", current_io=75.0, estimated_powerdraw=6.5, last_updated="2024-09-14T12:00:00Z")
        self.hdd_url = reverse('api/hdd')

    def test_get_hdd_list(self):
        """Test to retrieve the list of all HDDs."""
        response = self.client.get(self.hdd_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)  # Ensure that we get at least 1 item

    def test_create_hdd(self):
        """Test to create a new HDD."""
        data = {
            "model_number": "HUH721212ALE421",
            "current_io": 55.0,
            "estimated_powerdraw": 9.0,
            "last_updated": "2024-09-14T12:00:00Z",
            "disk_uuid":"268b-9037-33a0c848a2e4"
        }
        response = self.client.post(self.hdd_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HDDModel.objects.count(), 5)  # One created in setUp and one here
        self.assertEqual(HDDModel.objects.get(id=response.data['id']).model_number, "HUH721212ALE421")