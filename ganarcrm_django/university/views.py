from django.shortcuts import render
from requests import request

from rest_framework import viewsets

from .models import Result
from .serializers import ResultSerializer

class ResultViewSet(viewsets.ModelViewSet):
    serializer_class=ResultSerializer
    queryset=Result.objects.all()

