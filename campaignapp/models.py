from django.db import models




class BaseModel(models.Model):
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	date_deleted = models.DateField(null=True,blank=True)

	class Meta:
		abstract = True

class InterestBundle(BaseModel):
	name = models.CharField(max_length=120)

class Category(BaseModel):
	name = models.CharField(max_length=120)

class SubCategory(BaseModel):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	name = models.CharField(max_length=120)

class Interest(BaseModel):
	sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	name = models.CharField(max_length=120)


	
INTEREST_TYPE = (
	('BUNDLE',1),
	('PRECISE',2)
	)

class Address(BaseModel):
	type = models.CharField(max_length=120)
	value = models.CharField(max_length=120)

class Devices(BaseModel):
	desktop_browser = models.BooleanField(default=False)
	iphone = models.BooleanField(default=False)
	android = models.BooleanField(default=False)
	android_tablet = models.BooleanField(default=False)
	ipad = models.BooleanField(default=False)

class Scheduling(BaseModel):
	type = models.CharField(max_length=120)
	start_date = models.DateField()
	end_date = models.DateField()
	
class Campaign(BaseModel):
	interest_type = models.IntegerField(choices=INTEREST_TYPE)
	name = models.CharField(max_length=120)
	url = models.CharField(max_length=120)
	min_age = models.IntegerField()
	max_age = models.IntegerField()
	gender = models.CharField(max_length=120)
	price = models.FloatField()
	unique_visitors = models.IntegerField()
	price_per_day = models.IntegerField()

	address = models.ForeignKey(Address,on_delete=models.CASCADE)
	devices = models.ForeignKey(Devices,on_delete=models.CASCADE)
	scheduling = models.ForeignKey(Scheduling,on_delete=models.CASCADE)
	interest_bundle = models.ForeignKey(InterestBundle,on_delete=models.CASCADE,null=True,blank=True)



class CampaignInterest(BaseModel):
	campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)
	interest = models.ForeignKey(Interest,on_delete=models.CASCADE)




