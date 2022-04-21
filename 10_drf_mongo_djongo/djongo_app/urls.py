from django.urls import path, include
from rest_framework import routers
from .api_views import AccountViewSet, ShortLinkViewSet


djongo_router = routers.SimpleRouter()

djongo_router.register(
    r'accounts',
    AccountViewSet,
    basename='account',
)
# Use DRF nested routers
djongo_links_router = routers.NestedSimpleRouter(
    djongo_router,
    r'accounts',
    lookup='account',
)
djongo_links_router.register(
    r'links',
    ShortLinkViewSet,
    basename='account-link',
)

# Declare urlpatterns
urlpatterns = [

    # Djongo API
    path('djongo-api/', include(djongo_router.urls)),
    path('djongo-api/', include(djongo_links_router.urls)),
]