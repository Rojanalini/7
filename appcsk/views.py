from django.shortcuts import render
from django.http import HttpResponse
from msd.views import *


def msd(request):
    return HttpResponse(request,'msd.html')