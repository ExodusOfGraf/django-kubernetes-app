from django.urls import path
from .views import health_check, home

urlpatterns = [
    path('health/', health_check), # Для K8s проб
    path('', home),               # Главная страница
]
