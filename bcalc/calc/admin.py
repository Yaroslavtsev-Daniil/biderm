from django.contrib import admin
from .models import OptionsCategory, Option, Element


class OptionsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sort', 'subtitle', 'default_value',
    )
    list_editable = [
        'subtitle', 'default_value', 'sort',
    ]


class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sort', 'cost', 'subtitle',
    )
    list_editable = [
        'subtitle', 'cost', 'sort',
    ]
    list_filter = ['category']


class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sort', 'subtitle', 'coefficient', 'image',
    )
    list_editable = [
        'subtitle', 'coefficient', 'image', 'sort',
    ]


# Register your models here.
admin.site.register(OptionsCategory, OptionsCategoryAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Element, ElementAdmin)
