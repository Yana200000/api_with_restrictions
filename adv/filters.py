from django_filters import rest_framework as filters, CharFilter

from adv.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    status = CharFilter()
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
