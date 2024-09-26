from django.contrib import admin
from .models import BookPost


@admin.register(BookPost)
class PostAdmin(admin.ModelAdmin):
    """
    Custom admin panel with table view of property posts and picture preview
    """

    list_display = (
        "image_tag",
        "post_owner",
        "title",
        "slug",
        "accommodation_type",
        "city",
        "price_per_night",
        "created_on",
    )
    readonly_fields = ("image_tag",)
    search_fields = ["title", "content"]
    list_filter = (
        "city",
        "created_on",
    )


""" Cutom header naming """
admin.site.site_title = "Sweet Home Accommodation"
admin.site.index_title = "Administration panel"
admin.site.site_header = "Sweet Home Accommodation administrator panel"
