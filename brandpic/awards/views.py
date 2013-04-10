from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def my_awards(request):
	awards = request.user.profile.awards.all()
	return render_to_response('awards/my_awards.html',
		{'awards':awards},
		context_instance=RequestContext(request))