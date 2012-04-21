from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

class TagThreadManager(models.Manager):
    def get_subscribed(self, user, tag=None):
        usertags = user.get_profile().interests.all()
        if tag != None and tag in usertags:
            usertags = [tag]
        return self.filter(tags__in = usertags)

class TagThread(models.Model):
    subject = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add = True)

    objects = TagThreadManager()

    def __unicode__(self):
        return "%s: %s" % (self.created_date, self.subject)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        return super(TagThread, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tagmail_view_thread", args=[self.pk, self.slug])

class TagThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject",)}



class TagMessageManager(models.Manager):
    pass

class TagMessage(models.Model):
    sender = models.ForeignKey(User, verbose_name="From")
    body = models.TextField(verbose_name="Message")
    sent_date = models.DateTimeField(auto_now_add = True)
    thread = models.ForeignKey(TagThread, related_name="messages")

    objects = TagMessageManager()

    def __unicode__(self):
        return "%s - %s" % (self.sender, self.thread.subject)



admin.site.register(TagThread, TagThreadAdmin)
admin.site.register(TagMessage)
