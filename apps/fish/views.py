from django.views import generic

from apps.fish.models import Fish


class FishListView(generic.ListView):
    model = Fish
    template_name = 'index.html'
    context_object_name = 'fish'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class FishDetailView(generic.DetailView):
    model = Fish
    slug_field = 'slug'
    template_name = 'detail.html'
