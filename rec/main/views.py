from os import stat
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import subprocess
from time import sleep
from requests.models import Response
from .models import Outputs
from .serializers import outputSerializer
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.views import Response

# Create your views here.

'''
def index(request):
    url = "http://127.0.0.1:8000/commands/"
    data = requests.get(url).json()
    cmd = data[-1]['cmd']
    repetition = data[-1]['repetition']
    gap = data[-1]['gap']

    output = ""

    for i in range(int(repetition)):
        p = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output += p.stdout
        sleep(int(gap))

    out1 = Outputs()
    out1.op = output
    out1.save()

    # print(output)

    context = {"output": output}
    return render(request, "main.html", context)
'''


# API view
class outputList(APIView):

    # GET request
    def get(self, request):
        all_outputs = Outputs.objects.all()
        serializer = outputSerializer(all_outputs, many=True)
        return Response(serializer.data)

    # POST request
    def post(self, request):
        serializer = outputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
