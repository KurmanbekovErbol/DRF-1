from rest_framework.generics import CreateAPIView
from apps.main.models import Settings
from apps.main.serializer import SettingsSerializer

class CreatSettingsView(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer