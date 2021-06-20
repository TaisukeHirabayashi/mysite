from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("ようこそゴルフ部へ")

# Create your views here.
