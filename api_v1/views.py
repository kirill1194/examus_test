from rest_framework import mixins
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api_v1.authentication import SingleTokenAuthentication
from api_v1.serialziers import MenuItemSerializer
from core.models import MenuItem


@authentication_classes((SingleTokenAuthentication,))
@permission_classes((IsAuthenticated,))
class MenuItemApiViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = LimitOffsetPagination
