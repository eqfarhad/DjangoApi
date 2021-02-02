from rest_framework import serializers
from kayrrosApi.models import ShowsModel

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model=ShowsModel
        fields='__all__'

