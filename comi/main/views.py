from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.views import Response
from .models import commands
from .serializers import commandsSerializer
from .forms import ProductForm
import requests
# Create your views here


# api view
class commandsList(APIView):
    def get(self, request):
        comm1 = commands.objects.all()
        serializer = commandsSerializer(comm1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = commandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# input form
def comm_view(request):
    url = "http://127.0.0.1:8001/"
    data = requests.get(url).json()
    op = data[-1]['op']

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form, 'op': op}
    return render(request, 'my_form.html', context)
