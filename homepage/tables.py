import django_tables2 as tables
from homepage.models import EconomicRelease
from homepage.models import MADdash

class ECTable(tables.Table):
    class Meta:
        model = EconomicRelease
        Time = tables.Column(verbose_name="Time")
        Currency = tables.Column(verbose_name="Currency")
        Impact= tables.Column(verbose_name="Impact")
        Detail = tables.Column(verbose_name="Detail")
        Actual= tables.Column(verbose_name="Actual")
        Forecast = tables.Column(verbose_name="Forecast")
        Previous= tables.Column(verbose_name="Previous")
        # add class="paleblue" to <table> tag
        attrs = {"class": "ECTables"}

class MADdashTable(tables.Table):
    class Meta:
        model = MADdash
        fields = ('USD', 'M1', 'M5','M15','M30','H1',)
        USD = tables.Column(verbose_name="USD")
        M1 = tables.Column(verbose_name="M1")
        M5= tables.Column(verbose_name="M5")
        M15 = tables.Column(verbose_name="M15")
        M30 = tables.Column(verbose_name="M30")
        H1 = tables.Column(verbose_name="H1")
        # add class="paleblue" to <table> tag
        attrs = {"class": "ECTables"}




