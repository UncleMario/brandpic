from django.conf.urls import patterns, include, url

urlpatterns = patterns('brandpic.pictures.views',
    
    url(r'^post/$','post', name='post picture'),
    url(r'^my-pictures/$', 'my_pictures', name='my pictures'),
    url(r'^view/(?P<pictureID>\d+)/', 'view', name='view picture'),

) 