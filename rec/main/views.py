from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.


def index(request):
    url = "http://127.0.0.1:8000/commands/"
    data = requests.get(url).json()

    return HttpResponse(data)
