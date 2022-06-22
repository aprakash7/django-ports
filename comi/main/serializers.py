from .models import commands
from rest_framework import serializers


# serializer
class commandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = commands
        fields = "__all__"
