from django.urls import path,include
from rest_framework_nested import routers

from campaignapp import views

router = routers.DefaultRouter()
router.register('campaign',views.CampaignViewSet)
router.register('interestbundle',views.InterestBundleViewSet)
router.register('category',views.CategoryViewSet,'category')

category_router = routers.NestedSimpleRouter(router, r'category', lookup='category')
category_router.register(r'subcategory', views.SubcategoryViewSet, base_name='category-subcategory')


interest_router = routers.NestedSimpleRouter(category_router,r'subcategory',lookup='sub_category')
interest_router.register(r'interest',views.InterestViewSet,base_name='interest')





urlpatterns = [
	path('',include(router.urls)),
	path('',include(category_router.urls)),
	path('',include(interest_router.urls))
]