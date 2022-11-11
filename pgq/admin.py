from django.contrib import admin

from . import settings
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ("task", "queue", "created_at", "execute_at", "priority")

    def has_add_permission(self, request):
        # Hide the admin "+ Add" link for Jobs
        return False


if settings.SHOW_JOBS_ADMIN:
    admin.site.register(Job, JobAdmin)
