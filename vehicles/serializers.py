from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vehicle model.

    This serializer converts Vehicle instances to JSON format and vice versa.

    Meta:
    - model: Specifies the model to be serialized.
    - fields: Specifies the fields to be included in the serialization.
    """
    class Meta:
        model = Vehicle
        fields = '__all__'
