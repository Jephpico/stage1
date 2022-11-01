from rest_framework import serializers


class Slackdeets(serializers.Serializer):
    slackUsername = serializers.CharField()
    backend = serializers.BooleanField(default=False)
    age = serializers.IntegerField()
    bio = serializers.CharField(max_length=500)