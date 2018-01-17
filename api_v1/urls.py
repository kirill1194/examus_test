from django.urls.conf import path
from rest_framework.routers import SimpleRouter

from api_v1.views import MenuItemApiViewSet

urlpatterns = [
]

router = SimpleRouter()
router.register(r'menu_items', MenuItemApiViewSet, base_name='menu-items')

urlpatterns += router.urls
