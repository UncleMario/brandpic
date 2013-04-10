import json
import urllib

from django.http import HttpResponse
from django.core import serializers

from brandpic.brands.models import Brand

#Return Json with brand list
def brands_json(request):
	query = urllib.unquote(request.GET.get('query', '')) 
	query = query.strip()

	brands = serializers.serialize('python', Brand.objects.filter(name__contains=query))
	brands_dict = [brand['fields'] for brand in brands]

	return HttpResponse(json.dumps(brands_dict))


#Convert input from picture form to words
def input_to_words(var):
	words = var.split(",")
	return words

#Create brand instances
def add_brands(words, picture):
	names = [brand.name for brand in Brand.objects.all()]
	for word in words:
		if word not in names:
			brand = Brand.objects.create(name=word)
		else:
			brand = Brand.objects.filter(name=word)[0]
			brand.usage+=1
			brand.save()
		picture.brands.add(brand)


#Add brands for specific user
def add_brands_to_user(words, user):
	for word in words:
		brand = Brand.objects.filter(name__contains=word)[0]
		user.profile.brands.add(brand)




