from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from django.db.models import Max, Min
from django.core.paginator import Paginator
from django.conf import settings

from . import models
from . import filters

# Create your views here.

class Home(View):
    def get(self,request):
        slides = models.SlideImages.objects.all()
        sections = models.WebsiteSection.objects.all()
        return render(request,"items/index.html", {
            "sections": sections,
            "slides": slides,
        })

class Catalog(View):
    def get(self, request):
        items = models.Item.objects.all()
        p = Paginator(items, settings.ITEMS_PER_PAGE)
        page_number = request.GET.get("page") or 1
        items = p.get_page(page_number)
        return render(
            request, "items/catalog.html", {"items": items,  "p": p}
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


class Search(View):
    def get(self, request):
        if "term" in request.GET.keys():
            resp = models.Item.objects.filter(
                name__icontains=request.GET.get("term")
            ).values_list("name", flat=True)

            return JsonResponse(list(resp), safe=False)

        maxPrice = models.Item.objects.all().aggregate(Max("price"))["price__max"]
        minPrice = models.Item.objects.all().aggregate(Min("price"))["price__min"]
        items = models.Item.objects.all()
        filtered_items = filters.ItemFilter(request.GET, items)
        paginated = Paginator(filtered_items.qs, settings.ITEMS_PER_PAGE)
        page_number = request.GET.get("page") or 1
        items = paginated.get_page(page_number)

        try:
            title = request.GET.get("name__icontains") + " - Search Results"
        except:
            title = "Search Results"

        return render(
            request,
            "items/search.html",
            {
                "filter": filtered_items,
                "title": title,
                "maxPrice": maxPrice,
                "minPrice": minPrice,
                "items": items,
                "p": paginated,
            },
        )
