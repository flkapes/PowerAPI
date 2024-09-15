from django.db import models


# Create your models here.
class HDDModel(models.Model):
    model_number = models.CharField(max_length=100)
    disk_uuid = models.CharField(max_length=100)
    current_io = models.FloatField()
    estimated_powerdraw = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.estimated_powerdraw}W"


class CPUModel(models.Model):
    cpu_id = models.CharField(max_length=100)
    current_load = models.FloatField()
    estimated_powerdraw = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.estimated_powerdraw}W"


class GPUModel(models.Model):
    gpu_id = models.CharField(max_length=100)
    current_load = models.FloatField()
    estimated_powerdraw = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.estimated_powerdraw}W"
