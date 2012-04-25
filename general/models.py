from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class Skill(models.Model):
    #user_profiles = models.ManyToManyField(UserProfile, null=True, blank=True)
    title = models.CharField( max_length=30 )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'object_id': self.id})

    @classmethod
    def search(cls, q):
        return cls.objects.all().distinct().filter(
            Q(title__icontains=q)
            )


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    bio = models.TextField(blank=True)
    interests = TaggableManager( verbose_name='Interests', blank=True )
    location = models.CharField( max_length=100, blank=True )
    #city = models.CharField( max_length=50, blank=True )
    #state = models.CharField( max_length=50, blank=True )
    #postal_code = models.CharField( max_length=25, blank=True )
    url = models.URLField(blank=True)
    #skills = models.ManyToManyField(Skill, related_name='user_profiles', null=True, blank=True)
    avatar = models.ImageField(upload_to='/avatars/', blank=True, null=True)
    bg_image = models.ImageField(upload_to='/bg_images/', blank=True, null=True, verbose_name="Background image")

    def __unicode__(self):
        return self.user.__unicode__()

    def get_absolute_url(self):
        return reverse('general.views.view_profile', kwargs={'username':self.user.username})

def create_user_profile(sender, **kwargs):
    """ Creates a UserProfile for each new User """
    if kwargs['created'] == True:
        up = UserProfile(user=kwargs['instance'])
        up.save()
        
post_save.connect(create_user_profile, sender=User)


class Organization(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    description = models.TextField(blank = True)
    url = models.URLField(blank = True)
    addr1 = models.CharField(verbose_name = "Address", max_length = 255, blank = True)
    addr2 = models.CharField(verbose_name = "Address (cont.)", max_length = 255, blank = True)
    city = models.CharField(max_length = 255, blank = True)
    state = models.CharField(max_length = 255, blank = True)
    postal_code = models.CharField(max_length = 255, blank = True)
    members = models.ManyToManyField(User, related_name="organizations")
    admin = models.ForeignKey(User)
    resources = models.ManyToManyField('Resource', related_name='owners', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organization_detail', kwargs={'object_id': self.id})

    @classmethod
    def search(cls, q):
        return cls.objects.all().distinct().filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(city__icontains=q) |
            Q(state__icontains=q) |
            Q(postal_code__icontains=q)
            )


class Resource(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'object_id': self.id})

    @classmethod
    def search(cls, q):
        return cls.objects.all().distinct().filter(
            Q(name__icontains=q)
            )


admin.site.register(Resource)
admin.site.register(Organization)
admin.site.register(Skill)
admin.site.register(UserProfile)
