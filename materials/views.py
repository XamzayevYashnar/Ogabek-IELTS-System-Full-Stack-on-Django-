from django.db.models import Q
from django.views.generic import TemplateView

from .models import Folder, Material


class IndexView(TemplateView):
    template_name = 'materials/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()

        folders = Folder.objects.prefetch_related('materials').order_by('title')
        materials = Material.objects.select_related('folder').order_by('title')

        if query:
            materials = materials.filter(
                Q(title__icontains=query) | Q(folder__title__icontains=query)
            )

        context.update({
            'folders': folders,
            'materials': materials,
            'query': query,
        })
        return context
