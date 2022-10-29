from django_filters import rest_framework as filters, DateFromToRangeFilter, DateTimeFilter, AllValuesFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date = DateFromToRangeFilter()
    # created_at_before = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    # created_at_from = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    # update_up_before = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    # update_up_from = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    # title = AllValuesFilter(field_name='Advertisement__title')
    # creator = AllValuesFilter(field_name='Advertisement__creator')
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['date']
