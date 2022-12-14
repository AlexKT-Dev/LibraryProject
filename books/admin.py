from django.contrib import admin
from .models import *

admin.site.register(BooksModel)


class AdminBook(admin.ModelAdmin):
    search_fields = ('Title',)
    list_editable = ('SLUG', 'IS_PUBLISHED',)
    list_display = ['TITLE', 'SLUG', 'IS_PUBLISHED']
    list_display_links = ('TITLE',)
    list_filter = ('IS_PUBLISHED', 'TITLE', 'SLUG',)

    def _get_list_editable_queryset(self, request, prefix):
        list_editable = ('SLUG', 'IS_PUBLISHED',)
        return list_editable

    def get_search_fields(self, request):
        if (request.user.is_superuser):
            search_fields = ('SLUG', 'TITLE',)
            return search_fields
        else:
            search_field = ('TITLE',)
            return search_field

    def get_list_display_links(self, request, list_display):
        if (request.user.is_superuser):
            return list_display

    def get_list_filter(self, request):
        if (request.user.is_superuser):
            list_display = ['TITLE', 'SLUG', 'IS_PUBLISHED']
            return list_display
        else:
            list_display = ['IS_PUBLISHED']
            return list_display
