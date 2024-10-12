from datetime import datetime
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.test import TestCase

from user.models import User
from event.views import EventViewSet
from event.models import Event, EventCategory


factory = APIRequestFactory()


class TestEventViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        user, _ = User.objects.get_or_create(username="default")
        user.set_password("default")

        cls.user = user

        cls.category = EventCategory.objects.create(name="test", slug="test", user=cls.user)
        for i in range(10):
            Event.objects.create(
                title=f"test {i}",
                slug=f"test-{i}",
                category=cls.category,
                reminder_datetime=datetime.now(),
                user=cls.user,
            )

    @classmethod
    def tearDownClass(cls) -> None: ...

    def test_get_events(self):
        request = factory.get("/api/v1/events/")
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"get": "list"})
        response = event_viewset(request)
        self.assertEqual(len(response.data), 10)

    def test_get_event(self):
        event = self.category.event_set.first()
        request = factory.get("/api/v1/events/")
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"get": "retrieve"})
        response = event_viewset(request, pk=event.pk)
        self.assertEqual(event.title, response.data["title"])
        self.assertEqual(event.pk, response.data["id"])

    def test_create_event(self):
        event_data = {
            "title": "Go back to the future",
            "date": "2024-10-12",
            "time": "08:33:10",
            "category_name": "Hoby",
            "description": "enjoy",
        }

        request = factory.post("/api/v1/events/", data=event_data)
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"post": "create"})
        response = event_viewset(request)
        self.assertEqual(response.data["title"], "Go back to the future")
        self.assertEqual(response.data["category"]["name"], "Hoby")

    def test_update_event(self):
        event = self.category.event_set.first()
        event_data = {
            "title": "New days new hopes",
            "date": "2024-10-22",
            "time": "12:33:10",
            "category_name": "New Category",
        }

        request = factory.put("/api/v1/events/", data=event_data)
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"put": "update"})
        response = event_viewset(request, pk=event.pk)
        self.assertEqual(
            response.data["title"],
            "New days new hopes",
        )

    def test_delete_event(self):
        event = self.category.event_set.last()
        request = factory.delete("/api/v1/events/")
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"delete": "destroy"})
        response = event_viewset(request, pk=event.pk)
        self.assertEqual(response.status_code, 204)

    def test_get_upcoming_events(self):
        request = factory.get("/api/v1/events/upcoming/")
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"get": "list"})
        response = event_viewset(request)
        self.assertEqual(len(response.data), 10)

    def test_get_events_by_category_name(self):
        request = factory.get("/api/v1/events/category/")
        force_authenticate(request, self.user)
        event_viewset = EventViewSet.as_view({"get": "list"})
        response = event_viewset(request, categoryName=self.category.name)
        self.assertEqual(len(response.data), 10)
