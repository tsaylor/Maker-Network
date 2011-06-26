from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    subscriptions = TaggableManager()
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.__unicode__()

    def get_absolute_url(self):
        return reverse('general.views.view_profile')

admin.site.register(UserProfile)
