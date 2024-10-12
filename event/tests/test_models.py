from datetime import datetime

from django.test import TestCase

from ..models import Event, EventCategory
from user.models import User


class ModelCRUDTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = User.objects.create(username="testuser")

    @classmethod
    def tearDownClass(cls) -> None: ...

    def test_event_model_crud(self):
        right_now = datetime.now()
        slug = "test-event-title"
        event = Event.objects.create(
            user=self.user,
            title="Test Event Title",
            slug=slug,
            reminder_datetime=right_now,
            description="Test Event Description",
            category=EventCategory.objects.create(
                user=self.user, name="Test Category", slug="test-category"
            ),
        )
        self.assertEqual(event.pk, event.id)

        event = Event.objects.get(slug=slug)
        self.assertEqual(event.title, "Test Event Title")
        self.assertEqual(event.date, right_now.date())
        self.assertEqual(event.time, right_now.time())

        event.title = "Updated Title"
        event.save()
        event.refresh_from_db()

        self.assertEqual(event.title, "Updated Title")

        deleted = event.delete()
        self.assertEqual(str(deleted), "(1, {'event.Event': 1})")

    def test_event_category_model_crud(self):
        event_category = EventCategory.objects.create(
            name="Test Category", slug="test-category", user=self.user
        )

        self.assertEqual(event_category.pk, event_category.id)

        event_category = EventCategory.objects.get(slug="test-category")
        self.assertEqual(event_category.name, "Test Category")

        event_category.name = "Updated Category Name"
        event_category.save()
        event_category.refresh_from_db()

        self.assertEqual(event_category.name, "Updated Category Name")

        deleted = event_category.delete()
        self.assertEqual(str(deleted), "(1, {'event.EventCategory': 1})")
