from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin

from tastypie.api import Api

from brandpic.brands.functions import brands_json
from brandpic.brands.api.resources import PictureResource, BrandResource, UserResource
from tastypie_ext.resources import GETAPITokenAuthenticationResource
from tastypie_ext.resources import GETAPIFacebookTokenAuthenticationResource
from tastypie_ext.resources import POSTAPITokenAuthenticationResource, GETAPITokenAuthenticationResource
from tastypie_ext.resources import SessionResource
admin.autodiscover()

v1_api = Api(api_name='v1')

v1_api.register(UserResource())
v1_api.register(PictureResource())
v1_api.register(BrandResource())
v1_api.register(GETAPITokenAuthenticationResource())
v1_api.register(GETAPIFacebookTokenAuthenticationResource())
v1_api.register(SessionResource())
v1_api.register(POSTAPITokenAuthenticationResource())
v1_api.register(GETAPITokenAuthenticationResource())


urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template':'home.html'}),

    url(r'^logout/$', logout, {'next_page' : '/'}),

	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')),

    url(r'^profile/', include('brandpic.profile.urls')),
    url(r'^awards/', include('brandpic.awards.urls')),
    url(r'^pictures/', include('brandpic.pictures.urls')),
    url(r'^brands/', include('brandpic.brands.urls')),
    url(r'^brands_json/', brands_json),

    url(r'^api/', include(v1_api.urls)),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
