from django.urls import path
from .views import mssql_config_view

urlpatterns = [
    path('', mssql_config_view, name='mssql_config'),
]
