from rest_framework import serializers
from .models import *

# ==============================================================================
                            # Item-Type-Serializer
# ==============================================================================
class ItemTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = ItemsType
        fields = '__all__'

# ==============================================================================
                            # Department-Serializers
# ==============================================================================        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = '__all__'

# ==============================================================================
                            # Item-Serializer
# ==============================================================================
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
        

# ==============================================================================
                            # Vendor-Serializer
# ==============================================================================

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'