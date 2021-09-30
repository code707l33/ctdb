from rest_framework import serializers

from .models import Pilotadmin


class PilotadminModelSerializer(serializers.ModelSerializer):
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Pilotadmin
        exclude = ["adminpassword"]
