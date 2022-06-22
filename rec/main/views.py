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


class outputList(APIView):
    def get(self, request):
        all_outputs = Outputs.objects.all()
        serializer = outputSerializer(all_outputs, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
