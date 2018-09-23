from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers

from .models import Campaign,InterestBundle,Category,SubCategory,Interest,Address,Devices,Scheduling,Interest,CampaignInterest
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

	def list(self,request,category_pk, sub_category_pk):
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
				locations = data['location']
				address = Address.objects.create(
											type=locations['type'],
											value=locations['value']
											)
				device = data['device']
				if device.get('desktop_browser',False):
					devices = Devices.objects.create(desktop_browser=device['desktop_browser'])
				if device.get('iphone',False):
					devices = Devices.objects.create(iphone=device['iphone'])
				if device.get('android',False):
					devices = Devices.objects.create(android=device['android'])
				if device.get('android_tablet',False):
					devices = Devices.objects.create(android_tablet=device['android_tablet'])
				if device.get('ipad',False):
					devices = Devices.objects.create(ipad=device['ipad'])

				schedule = data['scheduling']
				scheduling = Scheduling.objects.create(
													type =  schedule['type'],
													start_date=schedule['start_date'],
													end_date=schedule['end_date']
													)


				Campaign.objects.create(name=data['name'],
										interest_type=data['interest_type'],
										url=data['url'],
										min_age=data['min_age'],
										max_age=data['max_age'],
										gender=data['gender'],
										price=data['price'],
										interest_bundle_id=data['interest_bundle_id'],
										unique_visitors=data['unique_visitors'],
										price_per_day=data['price_per_day'],
										address_id=address.id,
										devices_id=devices.id,
										scheduling_id=scheduling.id,


										)

									
				return Response(data)

			if data['interest_type'] == 2:
				locations = data['location']
				address = Address.objects.create(
											type=locations['type'],
											value=locations['value']
											)
				device = data['device']
				if device.get('desktop_browser',False):
					devices = Devices.objects.create(desktop_browser=device['desktop_browser'])
				if device.get('iphone',False):
					devices = Devices.objects.create(iphone=device['iphone'])
				if device.get('android',False):
					devices = Devices.objects.create(android=device['android'])
				if device.get('android_tablet',False):
					devices = Devices.objects.create(android_tablet=device['android_tablet'])
				if device.get('ipad',False):
					devices = Devices.objects.create(ipad=device['ipad'])

				schedule = data['scheduling']
				scheduling = Scheduling.objects.create(
													type =  schedule['type'],
													start_date=schedule['start_date'],
													end_date=schedule['end_date']
													)


				campaign = Campaign.objects.create(name=data['name'],
										interest_type=data['interest_type'],
										url=data['url'],
										min_age=data['min_age'],
										max_age=data['max_age'],
										gender=data['gender'],
										price=data['price'],
										unique_visitors=data['unique_visitors'],
										price_per_day=data['price_per_day'],
										address_id=address.id,
										devices_id=devices.id,
										scheduling_id=scheduling.id,
										)
				interests_id = data['interests']
				CampaignInterest.objects.create(campaign_id=campaign.id,
												interest_id=interests_id
												)
				return Response(data)



		else:
			raise serializers.ValidationError({
				'Detail':[serializer.errors]
				})
