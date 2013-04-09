from django.conf.urls import patterns, include, url

urlpatterns = patterns('brandpic.pictures.views',
    
    url(r'^post/$','post', name='post picture'),

) 