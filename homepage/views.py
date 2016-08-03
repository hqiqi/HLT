from django.shortcuts import render
from django.shortcuts import render_to_response

from .forms import SignUpForm
from .models import EconomicRelease
from .models import MADdash

from django_tables2 import RequestConfig
from homepage.models import EconomicRelease
from homepage.tables import ECTable
#from homepage.tables import MADdashTable

import datetime


# Create your views here.
def home(request):
	table = ECTable(EconomicRelease.objects.all())
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	#table2 = MADdashTable(MADdash.objects.all())
	now = datetime.datetime.now()

	#import oandapy

	#oanda = oandapy.API(environment="practice", access_token="10a0bc75e54c0f6aa7a51a4b702e370c-ca642fa0207516f2c1a57bb4f7785815")

	#response = oanda.get_prices(instruments="EUR_USD")

	context ={
		"home_title": title,
		"form": form,
		#"table":table,
		#"table2":table2,
		"now":now,
	}

	

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#print instance
		context ={
			"home_title": "Thank you!",
		}
	return render(request, "home.html", context,)

def people(request):
    table = ECTable(EconomicRelease.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'EconomicRelease.html', {'table': table})

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def tool(request):
	return render_to_response('tool.html')


    