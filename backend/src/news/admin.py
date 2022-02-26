from django.contrib import admin

from . import models


@admin.register(models.NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    """Новость."""

    date_hierarchy = 'date'
    ordering = ('subject', 'date',)

    list_display = ('subject', 'date',)

    list_filter = ('subject', 'date',)
    search_fields = ('subject', 'date',)

    class Meta:
        get_latest_by = ['-date']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
