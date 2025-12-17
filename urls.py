from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, currency_api, salary_report

router = DefaultRouter()
router.register('employees', EmployeeViewSet)

urlpatterns = router.urls + [
    path('currency/', currency_api),
    path('report/salary/', salary_report),
]
