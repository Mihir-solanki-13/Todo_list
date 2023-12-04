from django.contrib import admin
from .models import Task, Tag

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status', 'timestamp')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description', 'tags__value')

    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
        ('Timestamp', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )

class TagAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
