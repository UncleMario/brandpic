from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django_facebook.api import get_persistent_graph, require_persistent_graph
from django_facebook.decorators import facebook_required_lazy, facebook_required
from django_facebook.utils import next_redirect, parse_signed_request

from brandpic.pictures.forms import PictureForm

@login_required(login_url='/login/')
@facebook_required(scope='publish_stream,user_photos')
def post(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.save(commit=False)
			picture.owner = request.user
			picture.save()

			fb = get_persistent_graph(request)
			picture_to_upload = picture.get_url()
			fb.set('me/photos', url=picture_to_upload, message=picture.description)
			messages.info(request, 'Imagen subida correctamente')

			return HttpResponse('Imagen subida')
	else:
		form = PictureForm()
	return render_to_response('pictures/post.html', 
			{'form' : form}, 
			context_instance=RequestContext(request))





