from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers

from .models import Campaign,InterestBundle,Category,SubCategory,Interest
from .serializers import CampaignSerializer,InterestBundleSerializer

class InterestBundleViewSet(viewsets.ModelViewSet):
	queryset = InterestBundle.objects.all()
	serializer_class = InterestBundleSerializer

	def list(self,request):
		objects = self.queryset
		output = []
		for obj in objects:
			temp = {
			'id':obj.id,
			'name':obj.name

			}
			output.append(temp)
		return Response(output)

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = InterestBundleSerializer

	def list(self,request):
		objects = self.queryset
		output = []
		for obj in objects:
			temp = {
			'id':obj.id,
			'name':obj.name

			}
			output.append(temp)
		return Response(output)

class SubcategoryViewSet(viewsets.ModelViewSet):
	queryset = SubCategory.objects.all()
	serializer_class = InterestBundleSerializer

	def list(self,request,category_pk):
		print("list")
		ids = self.kwargs['category_pk']
		objects = SubCategory.objects.filter(category_id=ids)
		output = []

		for obj in objects:
			temp = {
			'id':obj.id,
			'name':obj.name,
			'Category_Name':obj.category.name

			}
			output.append(temp)
		return Response(output)

class InterestViewSet(viewsets.ModelViewSet):
	queryset = Interest.objects.all()
	serializer_class = InterestBundleSerializer

	def retrieve(self,request,sub_category_pk):
		print("list")
		ids = self.kwargs['sub_category_pk']
		objects = Interest.objects.filter(sub_category_id=ids)
		print(objects)
		output = []

		for obj in objects:
			temp = {
			'id':obj.id,
			'name':obj.name

			}
			output.append(temp)
		return Response(output)

class CampaignViewSet(viewsets.ModelViewSet):
	queryset = Campaign.objects.all()
	serializer_class = CampaignSerializer

	def create(self,request):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			data = serializer.data
			if data['interest_type'] == 1:
				Campaign.objects.create(name=data['name'],
										url=data['url'],
										min_age=data['min_age'],
										max_age=data['max_age'],
										gender=data['gender'],
										address_type=data['address_type'],
										address=data['address'],
										any_address=data['any_address'],
										devices=data['devices'],
										interest_type=data['interest_type'],
										price=data['price'],
										daily_visitors=data['daily_visitors'])
				return Response(data)

			if data['interest_type'] == 2:
				return Response("hello")

		else:
			raise serializers.ValidationError({
				'Detail':[serializer.errors]
				})
