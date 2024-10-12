from rest_framework import routers

from event.views import EventViewSet

__all__ = ["router_urls"]


router = routers.SimpleRouter()
router.register(r"events", EventViewSet, basename="events")
router_urls = router.urls
