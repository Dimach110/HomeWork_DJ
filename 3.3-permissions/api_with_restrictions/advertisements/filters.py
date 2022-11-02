from django_filters import rest_framework as filters, DateFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date = DateFromToRangeFilter(field_name="created_at")
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['date', 'creator']
