from django.conf.urls import patterns, include, url

urlpatterns = patterns('brandpic.brands.views',

    url(r'^my-brands/$','my_brands', name='my brands'),
 
) 