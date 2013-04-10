from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def my_brands(request):
	brands = request.user.profile.brands.all()
	return render_to_response('brands/my_brands.html',
		{'brands':brands},
		context_instance=RequestContext(request))