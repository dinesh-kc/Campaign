from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
import json
from json2html import *

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


def create_device_schedule(data):
	locations = data['location']
	loc_param = {'type': locations['type']}
	if locations['type'] != 'any':
		loc_param['value'] = locations['value']
	address = Address.objects.create(**loc_param)
	

	device = data['device']

	device_params = {}
	if device.get('desktop_browser',False):
		device_params['desktop_browser'] = True

	if device.get('iphone',False):
		device_params['iphone'] = True

	if device.get('android',False):
		device_params['android'] = True

	if device.get('android_tablet',False):
		device_params['android_tablet'] = True

	if device.get('ipad',False):
		device_params['ipad'] = True
		
	if device_params:
		device = Devices.objects.create(**device_params)

	else:
		device = Devices.objects.create(desktop_browser=True)

	schedule = data['scheduling']
	sc_params = {'type': schedule['type']}
	if schedule['type'] == 'manual':
		sc_params['start_date'] = schedule['start_date']
		sc_params['end_date'] = schedule['end_date']
	scheduling = Scheduling.objects.create(**sc_params)

	return address, device, scheduling

def send_email(data):
    r = send_mail(
    	'Campaign Data',
    	message='',
    	html_message=json2html.convert(json = data),
    	from_email='admin@%s'%settings.MAILGUN_SERVER_NAME,
    	recipient_list=['victgsheets@gmail.com', 'techackernp@gmail.com']
    	)


class CampaignViewSet(viewsets.ModelViewSet):
	queryset = Campaign.objects.all()
	serializer_class = CampaignSerializer

	def create(self,request):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			data = serializer.data
			
			if data['interest_type'] == "1":
				
				address, device, scheduling =  create_device_schedule(data)


				Campaign.objects.create(name=data['name'],
										interest_type=1,
										url=data['url'],
										min_age=data['min_age'],
										max_age=data['max_age'],
										gender=data['gender'],
										price=data['price'],
										interest_bundle_id=data['interest_bundle_id'],
										unique_visitors=data['unique_visitors'],
										price_per_day=data['price_per_day'],
										address_id=address.id,
										devices_id=device.id,
										scheduling_id=scheduling.id,


										)
				data['interests type'] = 'Bundle'
				send_email(data)				
				return Response(data)

			if data['interest_type'] == "2":

				address, device, scheduling =  create_device_schedule(data)

				campaign = Campaign.objects.create(name=data['name'],
										interest_type=2,
										url=data['url'],
										min_age=data['min_age'],
										max_age=data['max_age'],
										gender=data['gender'],
										price=data['price'],
										unique_visitors=data['unique_visitors'],
										price_per_day=data['price_per_day'],
										address_id=address.id,
										devices_id=device.id,
										scheduling_id=scheduling.id,
										)
				interests_id = data['interest']
				for i in interests_id:
					CampaignInterest.objects.create(campaign_id=campaign.id, interest_id=i)
				data['interests type'] = 'Precise'
				send_email(data)
				return Response(data)



		else:
			raise serializers.ValidationError({
				'Detail':[serializer.errors]
				})
