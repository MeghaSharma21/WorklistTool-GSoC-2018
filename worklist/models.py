from __future__ import unicode_literals
from django.db import models


# Model for table that contains the data
class WorkList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    theme = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    created_by = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    psid = models.IntegerField(blank=True)
    psid_added_by = models.CharField(max_length=100, blank=True)

    # Method to create a new entry in the table
    @staticmethod
    def create_object(data):
        WorkList.objects.create(name=data['name'],
                                theme=data['theme'],
                                description=data['description'],
                                created_by=data['created_by'],
                                psid=data['psid'],
                                psid_added_by=data['psid_added_by'])


