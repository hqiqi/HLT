from django.conf.urls import url
from django.contrib import admin

from .views import (
	indicator_list,
	indicator_MADdash,
	LotSizeCal,
	)

urlpatterns = [
	url(r'^$', indicator_list, name='list'),
    url(r'^MADdash/$', indicator_MADdash, name='MADdash'),
    url(r'^MADdash/LotSizeCal$', LotSizeCal, name='LotSizeCal'),
]