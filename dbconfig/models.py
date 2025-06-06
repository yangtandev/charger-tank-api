# dbconfig/models.py
from django.db import models

class MSSQLConfig(models.Model):
    label = models.CharField(max_length=100, default='default')
    driver = models.CharField(max_length=100, default='ODBC Driver 17 for SQL Server')
    host = models.CharField(max_length=100)
    port = models.PositiveIntegerField(default=1433)
    database = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    schema = models.CharField(max_length=100, default='dbo')
    table_name = models.CharField(max_length=100, default='ChargerTankHistory')

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label} - {self.host}:{self.port}/{self.database}"
