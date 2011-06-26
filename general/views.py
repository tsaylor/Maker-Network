from django.views.generic.create_update import update_object
from general.models import UserProfile


def view_profile(request):
    return edit_profile(request)

def edit_profile(request):
    return update_object(request, model=UserProfile, object_id=request.user.pk)
