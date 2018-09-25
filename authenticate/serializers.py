from rest_framework import serializers

class UserSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=120)

class UserLoginSerializer(serializers.Serializer):
	username = serializers.EmailField()
	password = serializers.CharField(max_length=120)
