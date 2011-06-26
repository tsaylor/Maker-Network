from django.shortcuts import render_to_response
from django.template import RequestContext

from tagmail.models import TagMessage

def anon_home(request):
    return render_to_response('anon_home.html', context_instance=RequestContext(request))

def home(request):
    if not request.user.is_authenticated():
        return anon_home(request)
    context = {"tagmessages":TagMessage.objects.all(),
               "subscribedtags":request.user.get_profile().subscriptions.all()}
    return render_to_response('home.html', context, context_instance=RequestContext(request))
