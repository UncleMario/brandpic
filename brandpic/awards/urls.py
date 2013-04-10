from django.conf.urls import patterns, include, url

urlpatterns = patterns('brandpic.awards.views',

	url(r'^my-awards/$','my_awards', name='my awards'),

) 