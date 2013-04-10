from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

#All brands of user
@login_required(login_url='/')
def my_brands(request):
	brands = request.user.profile.brands.all()
	return render_to_response('brands/my_brands.html',
		{'brands':brands},
		context_instance=RequestContext(request))


#Add new brand than user loves
@login_required(login_required='/')
def add(request):
	from brandpic.brands.functions import input_to_words, add_brands_to_user

	if request.method == 'POST':
		brands = request.POST['brands']
		words = input_to_words(brands)
		add_brands_to_user(words, request.user)
		return HttpResponseRedirect('/brands/my_brands')

	return render_to_response('brands/add.html', 
		{},
		context_instance=RequestContext(request))


