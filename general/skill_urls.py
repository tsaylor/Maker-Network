from django.conf.urls.defaults import *
from general.models import Skill

urlpatterns = patterns('',
    #url(r'^$', 'django.views.generic.list_detail.object_list', name='organization_list', kwargs={'queryset':Organization.objects.all()}),
    url(r'^(?P<object_id>[0-9]+)/$', 'django.views.generic.list_detail.object_detail', name='skill_detail', kwargs={'queryset':Skill.objects.all(), 'template_object_name':'skill'}),
)
