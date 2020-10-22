from rest_framework import routers
from .api import ChampionViewSet
from .constants import API_ENDPOINT

app_name = 'backend'

router = routers.DefaultRouter()
router.register(API_ENDPOINT, ChampionViewSet)

urlpatterns = router.urls
