from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from taggit.managers import TaggableManager

class TagMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(verbose_name="Message")
    sender = models.ForeignKey(User, verbose_name="From")
    tags = TaggableManager()

    def __unicode__(self):
        return "%s - %s" % (self.sender, self.subject)

admin.site.register(TagMessage)
