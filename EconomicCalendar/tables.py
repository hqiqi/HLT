import django_tables2 as tables
from EconomicCalendar.models import EconomicReleases

class ECT(tables.Table):
    class Meta:
        model = EconomicReleases
        fields = ('EventName', 'CountryCode', 'ReleasedOn','Consensus','Actual')
        orderable = False