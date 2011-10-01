from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^messages/', include('django.contrib.comments.urls')),


    url(r'^$', 'tagmail.views.home', name='home'),
    url(r'^view_thread/(?P<pk>\d*)/(?P<slug>[\w-]*)$', 'tagmail.views.view_thread', name='tagmail_view_thread'),
    
    url(r'^profile/', 'general.views.view_profile', name='profile'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if getattr(settings, 'MEDIA_SERVE', False):
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ) + urlpatterns

