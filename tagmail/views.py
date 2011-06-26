from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect

from taggit.models import Tag

from tagmail.models import TagThread, TagMessage
from tagmail.forms import NewThreadForm

def anon_home(request):
    return render_to_response('anon_home.html', context_instance=RequestContext(request))

def home(request):
    if not request.user.is_authenticated():
        return anon_home(request)

    if request.method == "POST":
        form = NewThreadForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            thread = TagThread(subject = form.cleaned_data['subject'])
            thread.save()
            thread.tags.add(*form.cleaned_data['tags'])
            message = TagMessage(sender = request.user,
                                 body = form.cleaned_data['body'],
                                 thread = thread)
            message.save()
            return HttpResponseRedirect(thread.get_absolute_url())
    else:
        form = NewThreadForm()

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
        tagthreads = TagThread.objects.get_subscribed(request.user)
    elif selected == "all-threads":
        tagthreads = TagThread.objects.all()
    else:
        tagthreads = TagThread.objects.get_subscribed(request.user, tag=selected)
    
    context = {"tagthreads":tagthreads,
               "subscribedtags":request.user.get_profile().subscriptions.all(),
               "selected":selected,
               "form":form,
              }
    return render_to_response('home.html', context, context_instance=RequestContext(request))

def view_thread(request, pk, slug):
    thread = TagThread.objects.get(pk = pk)
    return render_to_response('tagmail/view_thread.html', {'thread':thread}, context_instance=RequestContext(request))

