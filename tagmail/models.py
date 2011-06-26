from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from taggit.managers import TaggableManager

class TagMessageManager(models.Manager):
    def get_subscribed(self, user, tag=None):
        usertags = user.get_profile().subscriptions.all()
        if tag != None and tag in usertags:
            usertags = [tag]
        return self.filter(tags__in = usertags)

class TagMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(verbose_name="Message")
    sender = models.ForeignKey(User, verbose_name="From")
    tags = TaggableManager()

    objects = TagMessageManager()

    def __unicode__(self):
        return "%s - %s" % (self.sender, self.subject)

admin.site.register(TagMessage)
