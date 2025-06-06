# dbconfig/forms.py
from django import forms
from .models import MSSQLConfig

class MSSQLConfigForm(forms.ModelForm):
    class Meta:
        model = MSSQLConfig
        fields = ['label', 'driver', 'host', 'port', 'database', 'username', 'password', 'schema','table_name']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
