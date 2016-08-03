from django.conf.urls import url
from django.contrib import admin

from .views import (
	
	EconomicReleasess,
	)

urlpatterns = [
	url(r'^$', EconomicReleasess, name='list'),
    
]