from django.contrib import admin
from .models import ContactSubmission, DemoRequest


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'company', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'company', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']

    fieldsets = (
        ('Contact Info', {
            'fields': ('first_name', 'last_name', 'email', 'company')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'segment', 'status', 'created_at']
    list_filter = ['status', 'segment', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'company', 'goals']
    readonly_fields = ['created_at']
    list_editable = ['status']

    fieldsets = (
        ('Contact Info', {
            'fields': ('first_name', 'last_name', 'email', 'company', 'role')
        }),
        ('Request Details', {
            'fields': ('segment', 'goals')
        }),
        ('Internal', {
            'fields': ('status', 'notes', 'created_at')
        }),
    )