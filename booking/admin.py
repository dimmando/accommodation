from django.contrib import admin
from .models import BookPost


# Register your models here.

@admin.register(BookPost)
class PostAdmin(admin.ModelAdmin):

    list_display = ('image_tag', 'post_owner', 'title', 'slug', 'accommodation_type', 'city', 'price_per_night', 'created_on')
    readonly_fields = ('image_tag',)
    search_fields = ['title', 'content']
    list_filter = ('city', 'created_on',)

# admin.site.register(BookPost)

# class ImageThumb(admin.ModelAdmin):
#     list_display = ('image_tag',)  # Чтобы отобразить изображение в списке объектов
#     readonly_fields = ('image_tag',)  # Чтобы отобразить изображение в форме объекта

# admin.site.register(MyModel, ImageThumb)


admin.site.site_title = "Sweet Home Accommodation"
admin.site.index_title = "Administration panel"
admin.site.site_header = "Sweet Home Accommodation administrator panel"
