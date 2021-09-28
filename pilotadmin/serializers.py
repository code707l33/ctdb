from rest_framework import serializers

from .models import Pilotadmin


class PilotadminModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pilotadmin
        exclude = []
