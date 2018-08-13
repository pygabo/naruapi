from django.shortcuts import render
from ninjas.models import Nija, NijaImage, HiddenVillages
from rest_framework import viewsets
from .serializers import NijaSerializer


class NijaViewSet(viewsets.ModelViewSet):
    queryset = Nija.objects.all()
    serializer_class = NijaSerializer

