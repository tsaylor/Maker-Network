from django.views.generic.create_update import update_object
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import general.models as models


def view_profile(request):
    return edit_profile(request)

def edit_profile(request):
    return update_object(request, model=models.UserProfile, object_id=request.user.get_profile().pk)

def leave_organization(request, object_id):
    if request.method == "POST":
        org = get_object_or_404(models.Organization, id = object_id)
        org.members.remove(request.user)
        messages.add_message(request, messages.INFO, 'You have left %s' % org.name)
    return HttpResponseRedirect(reverse('organization_detail', kwargs={'object_id':org.id}))

def join_organization(request, object_id):
    if request.method == "POST":
        org = get_object_or_404(models.Organization, id = object_id)
        org.members.add(request.user)
        messages.add_message(request, messages.INFO, 'You have joined %s' % org.name)
    return HttpResponseRedirect(reverse('organization_detail', kwargs={'object_id':org.id}))
