from rest_framework import routers

from .views import CompanyViewSet

companies_routers = routers.DefaultRouter()
companies_routers.register(
    'companies',
    viewset=CompanyViewSet,
    basename='companies')


