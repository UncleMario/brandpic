from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template':'home.html'}),

    url(r'^logout/$', logout, {'next_page' : '/'}),

	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')),

    url(r'^profile/', include('brandpic.profile.urls')),
    url(r'^awards/', include('brandpic.awards.urls')),
    url(r'^pictures/', include('brandpic.pictures.urls')),
    url(r'^brands/', include('brandpic.brands.urls')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
