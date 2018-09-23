from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
	type = serializers.CharField(max_length=120)
	value = serializers.CharField(max_length=120,required=False,allow_blank=True)

class DeviceSerializer(serializers.Serializer):
	desktop_browser = serializers.BooleanField(required=False)
	iphone = serializers.BooleanField(required=False)
	android = serializers.BooleanField(required=False)
	android_tablet = serializers.BooleanField(required=False)
	ipad = serializers.BooleanField(required=False)

class SchedulingSerializer(serializers.Serializer):
	type = serializers.CharField(max_length=120)
	start_date = serializers.DateField()
	end_date = serializers.DateField()

class CampaignSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=120)
	url = serializers.CharField(max_length=120)
	min_age = serializers.IntegerField()
	max_age = serializers.IntegerField()
	gender = serializers.CharField(max_length=120)
	price = serializers.FloatField()
	interest_type = serializers.IntegerField()
	interest_bundle_id = serializers.IntegerField(required=False)
	unique_visitors = serializers.IntegerField()
	price_per_day = serializers.IntegerField()
	location = LocationSerializer()
	device = DeviceSerializer()
	scheduling = SchedulingSerializer()
	interests = serializers.ListField(required=False)



class InterestBundleSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=120)


