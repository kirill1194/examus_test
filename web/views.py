from builtins import sum

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from core.models import MenuItem


class IndexView(ListView):
    template_name = 'web/index.html'
    queryset = MenuItem.objects.all()


class Test(FormView):
    def form_valid(self, form):
        super().get_success_url()

class OrderView(View, TemplateResponseMixin):
    template_name = 'web/order.html'
    error_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        try:
            menu_items_ids = request.POST.getlist('ids', [])
            menu_items = MenuItem.objects.filter(id__in=menu_items_ids)
            price = sum([x.price for x in menu_items])
            context = {
                'items': menu_items,
                'price': price
            }
            return self.render_to_response(context=context)
        except Exception:
            return HttpResponseRedirect(self.error_url)

