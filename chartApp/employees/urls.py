from django.urls import path
from . import views

urlpatterns = [
    path('excelUpload/',views.excelUpload,name="excelUpload"),
    path('employees/', views.employees, name='employees'),
]
