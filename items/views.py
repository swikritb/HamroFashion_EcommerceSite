from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import AnonymousUser
from django.db.models import Max, Min
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.conf import settings

from . import models


# Create your views here.
class Home(View):
    def get(self, request):
        items = models.Item.objects.all()
        p = Paginator(items, settings.ITEMS_PER_PAGE)
        page_number = request.GET.get("page") or 1
        items = p.get_page(page_number)
        slides = models.SlideImages.objects.all()
        return render(
            request, "items/index.html", {"items": items, "slides": slides, "p": p}
        )


class ItemDetailView(DetailView):
    model = models.Item
    template_name = "items/detail.html"
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_context_data(self, **kwargs):
        context_data = super(ItemDetailView, self).get_context_data(**kwargs)
        context_data["title"] = context_data["object"].name
        return context_data
