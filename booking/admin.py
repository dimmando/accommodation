from django.contrib import admin
from .models import BookPost

@admin.register(BookPost)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'city', 'price_per_night', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('city', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.

# admin.site.register(BookPost)

admin.site.site_title = "Sweet Home Accommodation"
admin.site.site_header = "Sweet Home Accommodation administrator panel"
admin.site.index_title = "Administration panel"