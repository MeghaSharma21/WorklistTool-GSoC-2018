from __future__ import unicode_literals
from django.db import models


# Model for table that contains the data for Worklists
class WorkList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=300, blank=True)
    created_by = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    psid = models.IntegerField(blank=True)

    class Meta:
        unique_together = ('name', 'created_by')

    # Method to create a new entry in the table
    @staticmethod
    def create_object(data):
        worklist = WorkList.objects.create(name=data['name'],
                                tags=data.get('tags', ''),
                                description=data.get('description', ''),
                                created_by=data['created_by'],
                                psid=data.get('psid', 0))
        return worklist.id


# Model for table that contains the data for Tasks
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    worklist_id = models.IntegerField()
    article_id = models.IntegerField()
    psid = models.IntegerField(blank=True)
    description = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    effort = models.IntegerField(blank=True, null=True)
    claimed_by = models.CharField(max_length=100, blank=True)
    created_by = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('worklist_id', 'article_id')
        indexes = [
            models.Index(fields=['article_id'], name='article_id_idx'),
            models.Index(fields=['claimed_by'], name='claimed_by_idx'),
            models.Index(fields=['created_by'], name='created_by_idx'),

        ]

    # Method to create a new entry in the table
    @staticmethod
    def create_object(data):
        Task.objects.create(worklist_id=data['worklist_id'],
                            article_id=data['article_id'],
                            psid=data.get('has_psid', 0),
                            description=data.get('description', ''),
                            status=data.get('status', 0),
                            progress=data.get('progress', 0),
                            effort=data.get('effort', 0),
                            claimed_by=data.get('claimed_by', ''),
                            created_by=data['created_by'])


# Model for table that contains the data for Articles
class Articles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    avg_page_views = models.IntegerField(blank=True)
    projects = models.CharField(max_length=300, blank=True)
    size = models.IntegerField(blank=True)
    grade = models.CharField(max_length=300, blank=True)

    # Method to create a new entry in the table
    @staticmethod
    def create_object(data):
        Articles.objects.create(id=data['id'],
                                name=data['name'],
                                avg_page_views=data.get('avg_page_views', 0),
                                projects=data.get('projects', ''),
                                size=data.get('size', 0),
                                grade=data.get('grade', ''))
