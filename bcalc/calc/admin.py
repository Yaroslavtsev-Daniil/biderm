from django.contrib import admin
from .models import OptionsCategory, Option, Element, BasicDimentions


class OptionsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sort', 'slug', 'subtitle', 'default_value',
    )
    list_editable = [
        'slug', 'subtitle', 'default_value', 'sort',
    ]


class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'sort', 'cost', 'subtitle',
    )
    list_editable = [
        'subtitle', 'slug', 'cost', 'sort',
    ]
    list_filter = ['category']


class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'sort', 'subtitle', 'coefficient', 'image',
    )
    list_editable = [
        'subtitle', 'slug', 'coefficient', 'image', 'sort',
    ]


class BasicDimentionsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'width', 'height', 'depth', 'shelf_height',
    )
    list_editable = [
        'width', 'height', 'depth', 'shelf_height',
    ]



# Register your models here.
admin.site.register(OptionsCategory, OptionsCategoryAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(BasicDimentions, BasicDimentionsAdmin)
