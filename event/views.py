from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer

__all__ = ["EventViewSet"]


class EventViewSet(viewsets.ModelViewSet):
    """
    Event Viewset
    Includes CRUD operations
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset().filter(user_id=self.request.user.id).select_related("category")
        )

    @action(methods=["GET"], url_path="category/(?P<categoryName>[^/.]+)", detail=False)
    def get_events_by_category(self, request, **kwargs):
        category_name = kwargs.get("categoryName")
        queryset = self.filter_queryset(self.get_queryset()).filter(category__name=category_name)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["GET"], url_path="upcoming", detail=False)
    def get_upcoming_events(self, request, **kwargs):
        default_time_frame = 24
        right_now = timezone.now()
        today_plus_24_hours = right_now + timedelta(hours=default_time_frame)
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(
            reminder_datetime__gte=right_now, reminder_datetime__lte=today_plus_24_hours
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
