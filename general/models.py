from django.db import models
from django.db.models.signals import post_save
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

def create_user_profile(sender, **kwargs):
    """ Creates a UserProfile for each new User """
    if kwargs['created'] == True:
        up = UserProfile(user=kwargs['instance'])
        up.save()
        
post_save.connect(create_user_profile, sender=User)


admin.site.register(UserProfile)
