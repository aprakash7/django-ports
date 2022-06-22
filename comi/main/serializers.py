from .models import commands
from rest_framework import serializers


class commandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = commands
        fields = "__all__"
