from django.views.generic import ListView, DetailView

from apps.fish_food.models import FishFood


class FFoodListView(ListView):
    model = FishFood
    template_name = 'ffood_list.html'
    context_object_name = "fish_foods"


class FFoodDetailView(DetailView):
    model = FishFood,
    template_name = 'ffood_detail.html'
    context_object_name = "fish_food"
