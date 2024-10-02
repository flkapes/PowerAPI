from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import HDDModel, CPUModel, GPUModel

class HDDAPITests(APITestCase):
    def setUp(self):
        self.hdd = HDDModel.objects.create(model_number="HUH721212ALE622", disk_uuid="268b-a342-9037-33a0c848a2e4", current_io=75.0, estimated_powerdraw=6.5, last_updated="2024-09-14T12:00:00Z")
        self.hdd_url = reverse('hdd-list')

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
        self.assertEqual(HDDModel.objects.count(), 2)  # One created in setUp and one here
        self.assertEqual(HDDModel.objects.get(disk_uuid=response.data['disk_uuid']).model_number, "HUH721212ALE421")


class CPUAPITests(APITestCase):
    def setUp(self):
        self.cpu = CPUModel.objects.create(cpu_id="Intel i9-14900k", estimated_powerdraw=85.0, current_load=88.0, last_updated="2024-09-16T12:00:00Z")
        self.cpu_url = reverse("cpu-list")
    
    def test_get_cpu_list(self):
        """Test to retrieve the current CPU."""
        response = self.client.get(self.cpu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_cpu(self):
        """ Test to create a new CPU"""
        data = {
            "cpu_id": "Intel Xeon E5 - 2630 v4 @ 2.20GHz",
            "current_load": 30.0,
            "estimated_powerdraw": 45.0,
            "last_updated": "2024-09-16T12:00:00Z"
        }
        response = self.client.post(self.cpu_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CPUModel.objects.count(), 2)
        self.assertEqual(CPUModel.objects.get(cpu_id="Intel Xeon E5 - 2630 v4 @ 2.20GHz").estimated_powerdraw, 45.0)


class GPUAPITests(APITestCase):
    def setUp(self):
        self.gpu = GPUModel.objects.create(gpu_id="NVIDIA GeForce RTX 3090", estimated_powerdraw=350.0, current_load=95.0, last_updated="2024-09-16T12:00:00Z")
        self.gpu_url = reverse("gpu-list")

    def test_get_gpu_list(self):
        """Test to retrieve the list of all GPUs."""
        response = self.client.get(self.gpu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_gpu(self):
        """Test to create a new GPU."""
        data = {
            "gpu_id": "NVIDIA GeForce RTX 3080",
            "current_load": 90.0,
            "estimated_powerdraw": 320.0,
            "last_updated": "2024-09-16T12:00:00Z"
        }
        response = self.client.post(self.gpu_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GPUModel.objects.count(), 2)
        self.assertEqual(GPUModel.objects.get(gpu_id="NVIDIA GeForce RTX 3080").current_load, 90.0)