from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'



class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    """ list_editable = (
        'category'
    ) """
    search_fields = ('first_name',)
    list_filter = ('last_name',)
    list_display_links = ('birthday',)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )
    

admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)