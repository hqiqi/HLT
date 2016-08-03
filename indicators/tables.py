import django_tables2 as tables
from indicators.models import USD_MADdash
from indicators.models import EUR_MADdash
from indicators.models import GBP_MADdash
from indicators.models import JPY_MADdash
from indicators.models import AUD_MADdash
from indicators.models import NZD_MADdash
from indicators.models import CHF_MADdash
from indicators.models import CAD_MADdash



class USD_MADdashTable(tables.Table):
    class Meta:
        model = USD_MADdash
        fields = ('USD', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class EUR_MADdashTable(tables.Table):
    class Meta:
        model = EUR_MADdash
        fields = ('EUR', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class GBP_MADdashTable(tables.Table):
    class Meta:
        model = GBP_MADdash
        fields = ('GBP', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class JPY_MADdashTable(tables.Table):
    class Meta:
        model = JPY_MADdash
        fields = ('JPY', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class AUD_MADdashTable(tables.Table):
    class Meta:
        model = AUD_MADdash
        fields = ('AUD', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class NZD_MADdashTable(tables.Table):
    class Meta:
        model = NZD_MADdash
        fields = ('NZD', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class CHF_MADdashTable(tables.Table):
    class Meta:
        model = CHF_MADdash
        fields = ('CHF', 'M1', 'M5','M15','M30','H1',)
        orderable = False

class CAD_MADdashTable(tables.Table):
    class Meta:
        model = CAD_MADdash
        fields = ('CAD', 'M1', 'M5','M15','M30','H1',)
        orderable = False


