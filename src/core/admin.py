from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_handled")
    list_filter = ("is_handled", "created_at")
    search_fields = ("name", "email", "subject", "message")