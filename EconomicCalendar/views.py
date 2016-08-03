from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django_tables2 import RequestConfig

from .tables import ECT
from .models import EconomicReleases
# Create your views here.
def EconomicReleasess(request):

	Ectable1 = ECT(EconomicReleases.objects.all())
	
	context ={
		"Ectable1":Ectable1,
	}
	return render(request, 'EconomicRelease.html', context)