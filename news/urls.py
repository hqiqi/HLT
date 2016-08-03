from django.conf.urls import url
from django.contrib import admin

from .views import (
	news_list,
	news_create,
	news_detail,
	news_update,
	news_delete,
	)

urlpatterns = [
	url(r'^$', news_list, name='list'),
    url(r'^create/$', news_create),
    url(r'^(?P<slug>[\w-]+)/$', news_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', news_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', news_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
