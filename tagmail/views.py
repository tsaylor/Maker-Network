from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from taggit.models import Tag

from tagmail.models import TagMessage

def anon_home(request):
    return render_to_response('anon_home.html', context_instance=RequestContext(request))

def home(request):
    if not request.user.is_authenticated():
        return anon_home(request)

    selected = None
    if "tag" in request.GET.keys():
        try:
            selected = Tag.objects.get(slug=request.GET.get('tag', None))
        except Tag.DoesNotExist, Tag.MultipleObjectsReturned:
            messages.error(request, 'There was an error with the tag "%s"' % request.GET.get('tag', None))
            selected = "all-your-threads"
    if "special" in request.GET.keys():
        selected = request.GET.get('special', None)
    if selected == None:
        selected = "all-your-threads"

    tagthreads = None
    if selected == "all-your-threads":
        tagthreads = TagMessage.objects.get_subscribed(request.user)
    elif selected == "all-threads":
        tagthreads = TagMessage.objects.all()
    else:
        tagthreads = TagMessage.objects.get_subscribed(request.user, tag=selected)
    
    context = {"tagthreads":tagthreads,
               "subscribedtags":request.user.get_profile().subscriptions.all(),
               "selected":selected,
              }
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def view_thread(request, pk):
    message = TagMessage.objects.get(pk = pk)
    return render_to_response('tagmail/view_thread.html', {'message':message}, context_instance=RequestContext(request))
    
