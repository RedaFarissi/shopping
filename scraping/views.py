from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def test(request):
    content = requests.get("https://shoptout.ma/high-tech.html")
    return HttpResponse(content.text)