from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('report-found/', views.report_found_pet, name='report_found_pet'),
]
