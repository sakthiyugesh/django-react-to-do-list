from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serilaizers import listSerializers
from .models import *
from rest_framework import viewsets


class Todolists(viewsets.ModelViewSet):
    queryset = Lists.objects.all()
    serializer_class = listSerializers