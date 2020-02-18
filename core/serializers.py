from rest_framework import serializers

from core.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format="%H:%M %p %d-%m-%Y")

    class Meta:
        model = Tweet
        fields = ('id', 'name', 'message', 'datetime')
