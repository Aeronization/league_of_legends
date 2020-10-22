
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls', 'frontend')),
    path('', include('backend.urls', 'backend')),
    # path('accounts/', include('allauth.urls')),
]
