from django.core.mail import send_mail

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Company
from .serializers import CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination

# this decorator turns the function in a post method
@api_view(http_method_names = ['POST'])
def send_company_email(request):
    send_mail(subject=request.data.get("subject"), message=request.data.get("message"), from_email="robinson_fisp@yahoo.com.br", recipient_list=["robinsonbrz@gmail.com"])
    return Response({"status":"success","info":"email sent successfully", }, status=200)



