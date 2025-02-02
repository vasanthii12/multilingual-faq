from django.contrib import admin
from .models import FAQ



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'created_at')
    list_filter = ('language', 'created_at')
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('question', 'answer', 'language')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
