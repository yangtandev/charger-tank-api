# dbconfig/views.py
from django.shortcuts import render, redirect
from .forms import MSSQLConfigForm
from .models import MSSQLConfig
import pyodbc

def mssql_config_view(request):
    # Read the saved settings
    config = MSSQLConfig.objects.filter(label='default').first()

    if request.method == 'POST':
        form = MSSQLConfigForm(request.POST, instance=config)
        if form.is_valid():
            config = form.save()

            # test connection
            conn_str = (
                f"DRIVER={{{config.driver}}};"
                f"SERVER={config.host},{config.port};"
                f"DATABASE={config.database};"
                f"UID={config.username};"
                f"PWD={config.password};"
                f"TrustServerCertificate=yes;"
            )
            try:
                with pyodbc.connect(conn_str, timeout=5) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT GETDATE();")
                    result = cursor.fetchone()[0]
                error = None
            except Exception as e:
                result = None
                error = str(e)

            return render(request, 'dbconfig/mssql_config.html', {
                'form': form,
                'result': result,
                'error': error,
            })
    else:
        form = MSSQLConfigForm(instance=config)

    return render(request, 'dbconfig/mssql_config.html', {
        'form': form,
    })
