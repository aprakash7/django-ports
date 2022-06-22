from .models import Outputs
from rest_framework import serializers


# serializer
class outputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outputs
        fields = "__all__"
