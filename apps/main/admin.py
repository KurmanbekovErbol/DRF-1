from django.contrib import admin
from apps.main.models import Settings
# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)