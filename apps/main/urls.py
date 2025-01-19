from django.urls import path
from apps.main.views import CreatSettingsView

urlpatterns = [
    path("settings/create/", CreatSettingsView.as_view(), name="settings_create")
]