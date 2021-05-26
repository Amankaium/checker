from django.contrib import admin
from .models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ["url", "user", "interval",
                    "is_paused", "created_at", "updated_at"]
    
    fields = ["url", "user", "interval", "is_paused",
              "created_at", "updated_at"]
    
    readonly_fields = ["created_at", "updated_at"]
    
    search_fields = ["user__username", "user__first_name",
                     "user__last_name", "user__email", "url"]
    
    list_filter = ["is_paused", "created_at", "updated_at"]





