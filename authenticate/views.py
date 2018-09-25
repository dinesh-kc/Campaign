from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.response import Response

from django.contrib.auth.models import User

from .serializers import UserSerializer,UserLoginSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self,request):
		print('create')
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			data = serializer.data
			user,created = User.objects.get_or_create(email=data['email'],defaults={
										'username':data['email']
										})
			if created:
				user.set_password(data['password'])
				user.save()
			return Response(data)
		else:
			raise serializers.ValidationError({
				'Detail':[serializer.errors]
				})
class UserLoginViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserLoginSerializer

	def create(self,request):
		username = request.data.get("username")
		password = request.data.get("password")

		user = authenticate(username=username,password=password)
		if not user:
			raise serializers.ValidationError({
				'Detail':['Error username And password']
				})
		token,created = Token.objects.get_or_create(user=user)
	
		return Response({"token":token.key,"id":user.id})


	