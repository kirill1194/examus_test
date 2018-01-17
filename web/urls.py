from django.urls.conf import path

from web.views import IndexView, OrderView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('order', OrderView.as_view(), name='order')
]