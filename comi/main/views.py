from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response
from .models import commands
from .serializers import commandsSerializer
# Create your views here


class commandsList(APIView):
    def get(self, request):
        comm1 = commands.objects.all()
        serializer = commandsSerializer(comm1, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
