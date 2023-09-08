from django.contrib import admin
from . import models
from django.core import serializers
from django.http import HttpResponse


# Register your models here.
admin.site.register(
    [
        models.Photo,
        models.SlideImages,
        models.WebsiteSection
    ]
)


class ItemAdmin(admin.ModelAdmin):
    search_fields = ("name", "price")
    list_filter = (
        "status",
        "date_added",
    )
    exclude = ("code", "real_time_price")
    list_display = ("name", "Price", "is_available")
    actions = ["make_out_of_stock", "make_in_stock", "export_as_json"]
    ordering = ["-date_added"]

    def make_out_of_stock(self, request, queryset):
        queryset.update(status="out of stock")

    make_out_of_stock.short_description = "Mark Unavailable"

    def make_in_stock(self, request, queryset):
        queryset.update(status="instock")

    make_out_of_stock.short_description = "Mark Available"

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    def Price(self, obj):
        return "NRS " + str(obj.real_time_price)


admin.site.register(models.Item, ItemAdmin)
