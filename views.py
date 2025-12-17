from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from .models import Employee
from .serializers import EmployeeSerializer

# CRUD APIs
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Third-party API integration
@api_view(['GET'])
def currency_api(request):
    r = requests.get('https://api.exchangerate-api.com/v4/latest/INR')
    data = r.json()
    return Response({
        "USD": data["rates"]["USD"],
        "EUR": data["rates"]["EUR"]
    })

# Reporting API (Visualization-ready)
@api_view(['GET'])
def salary_report(request):
    data = Employee.objects.values('department').annotate(
        avg_salary=Avg('salary')
    )
    return Response(data)

