from django.contrib import admin
from .models import BugReport, FeatureRequest



# Класс администратора для модели Project
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task',
                    'status', 'priority', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority')
    list_editable = ('status', 'priority')
    # ordering = ('created_at',)
    # date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'priority')
        }),
        ('Additional Information', {
            'fields': ('status', 'project', 'task'),
            'classes': ('collapse',)
        }),
    )

# Класс администратора для модели Task
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description', 'created_at')
    list_editable = ('status', 'priority')
    editable = True
