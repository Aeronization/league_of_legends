from .models import Champion
from .serializers import ChampionSerializer
from rest_framework import viewsets, permissions

# Champion ViewSet.
class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChampionSerializer