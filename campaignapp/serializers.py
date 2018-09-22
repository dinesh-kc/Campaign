from rest_framework import serializers

class CampaignSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=120)
	url = serializers.CharField(max_length=120)
	min_age = serializers.IntegerField()
	max_age = serializers.IntegerField()
	gender = serializers.IntegerField()
	address_type = serializers.IntegerField()
	address = serializers.CharField(max_length=120)
	any_address = serializers.CharField(max_length=120,required=False)
	devices = serializers.IntegerField()
	price = serializers.FloatField()
	interest_type = serializers.IntegerField()
	daily_visitors = serializers.IntegerField()

class InterestBundleSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=120)


