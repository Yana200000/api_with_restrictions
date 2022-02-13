from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from adv.models import Advertisement
from adv.serializers import AdvertisementSerializer
from adv.permissions import IsOwnerOrReadOnly
from adv.filters import AdvertisementFilter

from django_filters.rest_framework import DjangoFilterBackend


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create']:
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []
