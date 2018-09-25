from django.contrib import admin

from .models import *


class InterestBundleAdmin(admin.ModelAdmin):
    list_display = [a.name for a in InterestBundle._meta.fields]

admin.site.register(InterestBundle, InterestBundleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Category._meta.fields]

admin.site.register(Category, CategoryAdmin)



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [a.name for a in SubCategory._meta.fields]

admin.site.register(SubCategory, SubCategoryAdmin)



class InterestAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Interest._meta.fields]

admin.site.register(Interest, InterestAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Address._meta.fields]

admin.site.register(Address, AddressAdmin)



class DevicesAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Devices._meta.fields]

admin.site.register(Devices, DevicesAdmin)



class SchedulingAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Scheduling._meta.fields]

admin.site.register(Scheduling, SchedulingAdmin)

class CampaignAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Campaign._meta.fields]

admin.site.register(Campaign, CampaignAdmin)



class CampaignInterestAdmin(admin.ModelAdmin):
    list_display = [a.name for a in CampaignInterest._meta.fields]

admin.site.register(CampaignInterest, CampaignInterestAdmin)




# admin.site.register(InterestBundle)
# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(Interest)
# admin.site.register(Campaign)