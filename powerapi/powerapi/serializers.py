from rest_framework import serializers
from .models import HDDModel, GPUModel, CPUModel

class HDDModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDDModel
        fields = ['model_number', 'disk_uuid', 'current_io', "estimated_powerdraw", "last_updated"]
        
class GPUModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPUModel
        fields = ['gpu_id', 'current_load', "estimated_powerdraw", "last_updated"]

class CPUModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUModel
        fields = ['cpu_id', 'current_load', "estimated_powerdraw", "last_updated"]