from django.views.generic import ListView, DetailView

from apps.accessories.models import Accessory


class AccessoryListView(ListView):
    model = Accessory
    template_name = 'accessory_list.html'
    context_object_name = 'accessories'


class AccessoryDetailView(DetailView):
    model = Accessory
    template_name = 'accessory_detail.html'
    context_object_name = 'accessory'
