from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    moderator = models.ForeignKey(User, related_name='+')
    name      = models.CharField(max_length=32)
    members   = models.ManyToManyField(User, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    project     = models.ForeignKey(Project)
    title       = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_estimated_by(self):
        return [e.user for e in self.estimate_set.all()]

    def __unicode__(self):
        return self.title


class Estimate(models.Model):
    story       = models.ForeignKey(Story)
    user        = models.ForeignKey(User)
    points      = models.SmallIntegerField()
    comment     = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
