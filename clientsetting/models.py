from django.db import models

class ClientSetting(models.Model):
    name = models.CharField(max_length=30,
                            blank=False,
                            null=False,
                            unique=True,
                            primary_key=True)
    group = models.CharField(max_length=20,
                             blank=True,
                             null=True)
    value = models.CharField(max_length=500,
                             blank=True,
                             null=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'clientsetting'
    def __str__(self):
        return f'{self.name}, last_modified: {self.last_modified}'
