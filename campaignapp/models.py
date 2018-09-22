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

GENDER = (
	('MALE',1),
	('FEMALE',2)
	)

ADDRESS_TYPE = (
	('COUNTRY',1),
	('STATE',2),
	('CITY',3)
	)
DEVICE = (
	('MOBILE',1),
	('DESKTOP',2)
	)
	
INTEREST_TYPE = (
	('BUNDLE',1),
	('PRECISE',2)
	)

class Campaign(BaseModel):
	name = models.CharField(max_length=120)
	url = models.CharField(max_length=120)
	min_age = models.IntegerField()
	max_age = models.IntegerField()
	gender = models.IntegerField(choices=GENDER)
	address_type = models.IntegerField(choices=ADDRESS_TYPE)
	address = models.CharField(max_length=120,null=True)
	any_address = models.CharField(max_length=120,blank=True,null=True)
	devices = models.IntegerField(choices=DEVICE)
	interest_type = models.IntegerField(choices=INTEREST_TYPE)
	interest_bundle = models.ForeignKey(InterestBundle,on_delete=models.CASCADE,null=True,blank=True)
	price = models.FloatField()
	daily_visitors = models.IntegerField()


