from django.contrib.auth.models import User

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie_ext.authentication import FacebookOAUTH2Authentication
from brandpic.brands.models import Brand
from brandpic.pictures.models import Picture


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		authentication = FacebookOAUTH2Authentication()
		authorization = DjangoAuthorization()


class PictureResource(ModelResource):
	owner = fields.ForeignKey(UserResource, 'owner')
	
	class Meta:
		queryset = Picture.objects.all()
		resource_name = 'picture'
		filtering = {
			'owner' : ALL_WITH_RELATIONS,
			'date' : ['exact', 'lt', 'lte', 'gte', 'gt'],
		}


class BrandResource(ModelResource):
	class Meta:
		queryset = Brand.objects.all()
		resource_name = 'brand'
		authentication = FacebookOAUTH2Authentication()
		authorization = Authorization()
		





			
