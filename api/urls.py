from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import ResourceHandler, OrganizationHandler, UserHandler

resource_handler = Resource(ResourceHandler)
organization_handler = Resource(OrganizationHandler)
user_handler = Resource(UserHandler)

urlpatterns = patterns('',
    url(r'^resource/(?P<id>[^/]+)/', resource_handler),
    url(r'^resources/', resource_handler),
    url(r'^organization/(?P<id>[^/]+)/', organization_handler),
    url(r'^organizations/', organization_handler),
    url(r'^users/', user_handler),
)
