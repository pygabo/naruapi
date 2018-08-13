from ninjas.models import Nija, NijaImage, HiddenVillages
from rest_framework import serializers


class NijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nija
        fields = '__all__'
