from django_filters import rest_framework as filters

from .models import CurrencyModel


class CurrencyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    exponent = filters.NumberFilter(field_name='exponent')
    country = filters.CharFilter(field_name='countries__name', lookup_expr='icontains')
    exact_country = filters.CharFilter(field_name='countries__name', lookup_expr='iexact')
    capital = filters.CharFilter(field_name='countries__capital', lookup_expr='icontains')


    class Meta:
        model = CurrencyModel
        fields = [
            'code',
            'name',
            'exponent',
            'country',
            'exact_country',
            'capital'
        ]