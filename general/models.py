from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    subscriptions = TaggableManager()
    city = models.CharField( max_length=50 )
    state = models.CharField( max_length=50 )
    postal_code = models.CharField( max_length=25 )
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

class Skill(models.Model):
    user_profile = models.ManyToManyField(UserProfile)
    title = models.CharField( max_length=30 )

#    def __unicode__(self):
#        return self.user_profile.__unicode__()
