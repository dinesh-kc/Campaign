from django.contrib import admin

from .models import InterestBundle,Category,SubCategory,Interest,Campaign

admin.site.register(InterestBundle)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Interest)
admin.site.register(Campaign)