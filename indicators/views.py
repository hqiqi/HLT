from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string

from .models import USD_MADdash
from .models import EUR_MADdash
from .models import GBP_MADdash
from .models import JPY_MADdash
from .models import AUD_MADdash
from .models import NZD_MADdash
from .models import CHF_MADdash
from .models import CAD_MADdash


from django_tables2 import RequestConfig

from .tables import USD_MADdashTable
from .tables import EUR_MADdashTable
from .tables import GBP_MADdashTable
from .tables import JPY_MADdashTable
from .tables import AUD_MADdashTable
from .tables import NZD_MADdashTable
from .tables import CHF_MADdashTable
from .tables import CAD_MADdashTable


def indicator_list(request):
	return render_to_response('indicator_list.html')

def indicator_MADdash(request):


	Mtable1 = USD_MADdashTable(USD_MADdash.objects.all())
	Mtable2 = EUR_MADdashTable(EUR_MADdash.objects.all())
	Mtable3 = GBP_MADdashTable(GBP_MADdash.objects.all())
	Mtable4 = JPY_MADdashTable(JPY_MADdash.objects.all())
	Mtable5 = AUD_MADdashTable(AUD_MADdash.objects.all())
	Mtable6 = NZD_MADdashTable(NZD_MADdash.objects.all())
	Mtable7 = CHF_MADdashTable(CHF_MADdash.objects.all())
	Mtable8 = CAD_MADdashTable(CAD_MADdash.objects.all())
	
	context ={
		"Mtable1":Mtable1,
		"Mtable2":Mtable2,
		"Mtable3":Mtable3,
		"Mtable4":Mtable4,
		"Mtable5":Mtable5,
		"Mtable6":Mtable6,
		"Mtable7":Mtable7,
		"Mtable8":Mtable8,
	}
	return render(request, 'MADdash.html', context)

def LotSizeCal(request):
    return render_to_response('LotSizeCal.html')
 