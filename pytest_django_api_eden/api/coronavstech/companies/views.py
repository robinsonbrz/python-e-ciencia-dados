from django.shortcuts import render
from .serializers import CompanySerializer
from rest_framework.pagination import PageNumberPagination

class CompanyViewSet(ModelViewset):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by('-last_update')
    pagination_class = PageNumberPagination

    