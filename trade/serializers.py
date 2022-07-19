from rest_framework import serializers
from .models import Client


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'client',
        )
        model = Client