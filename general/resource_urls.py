from django.conf.urls.defaults import *
from general.models import Resource

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', name='resource_list', kwargs={'queryset':Resource.objects.all()}),
    url(r'^(?P<object_id>[0-9]+)/$', 'django.views.generic.list_detail.object_detail', name='resource_detail', kwargs={'queryset':Resource.objects.all(), 'template_object_name':'resource'}),
    url(r'^(?P<resource_id>[0-9]+)/add/$', 'general.views.add_resource', name='resource_add'),
    url(r'^(?P<resource_id>[0-9]+)/remove/$', 'general.views.remove_resource', name='resource_remove'),
)
