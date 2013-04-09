from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin


from facebook.views import login as login_facebook, authentication_callback

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^', include('brandpic.home.urls')),

    url(r'^login/$',  login),
    url(r'^logout/$', logout, {'next_page' : '/'}),


    url(r'^facebook/login$', login_facebook),
    url(r'^facebook/authentication_callback$', authentication_callback),
    
    url(r'^profile/', include('brandpic.profile.urls')),
    url(r'^awards/', include('brandpic.awards.urls')),
    url(r'^pictures/', include('brandpic.pictures.urls')),
    url(r'^brands/', include('brandpic.brands.urls')),
    

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
