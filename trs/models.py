from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=400, null=True, blank=True)


class Task(models.Model):
    name = models.CharField(max_length=100, blank=False)
    project = models.ForeignKey('Project', related_name='tasks')