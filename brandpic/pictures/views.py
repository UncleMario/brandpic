from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django_facebook.api import get_persistent_graph, require_persistent_graph
from django_facebook.decorators import facebook_required_lazy, facebook_required
from django_facebook.utils import next_redirect, parse_signed_request

from brandpic.pictures.forms import PictureForm
from brandpic.pictures.models import Picture
from brandpic.brands.functions import input_to_words, add_brands

#Upload photo whith love for your favorities brands
@login_required(login_url='/login/')
@facebook_required(scope='publish_stream,user_photos')
def post(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.save(commit=False)
			picture.owner = request.user
			picture.save()

			#Adding brands to picture
			words = input_to_words(request.POST['brands'])
			add_brands(words, picture)

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


#View all pictures uploaded by you
@login_required(login_url='/login/')
def my_pictures(request):
	pictures = Picture.objects.all()
	return render_to_response('pictures/my_pictures.html',
		{'pictures':pictures},
		context_instance=RequestContext(request))





