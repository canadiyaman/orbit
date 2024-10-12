import random
from datetime import datetime
from typing import List

from django.core.management import BaseCommand
from django.db import IntegrityError
from django.utils.text import slugify

from event.models import Event, EventCategory
from user.models import User


class Command(BaseCommand):
    help = "Generates initial events and categories"

    def add_arguments(self, parser):
        parser.add_argument(
            "-c", nargs="?", type=int, help="Count of Event wanted to create (default: 100)"
        )
        parser.add_argument(
            "-cn",
            nargs="?",
            type=str,
            help="You can give category names with using to separate with comma (eg. Work,Spor)",
        )

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username="default")
        user.set_password("default")
        user.save()

        len_of_data = options.get("count") or 100

        category_names = options.get("category_names") or ""
        category_objects = self._handle_category_names(category_names, user)
        len_of_categories = len(category_objects)

        for i in range(len_of_data):
            try:
                category_obj = category_objects[random.randint(0, len_of_categories)]
            except IndexError:
                category_obj = category_objects[0]

            try:
                title = f"Random event about {category_obj.name} {i}"
                event, _ = Event.objects.get_or_create(
                    title=title,
                    slug=slugify(title),
                    category=category_obj,
                    defaults={
                        "user": user,
                        "reminder_datetime": datetime(
                            day=random.randint(1, 28),
                            month=random.randint(1, 12),
                            hour=random.randint(0, 23),
                            minute=random.randint(0, 59),
                            second=random.randint(0, 59),
                            year=2025,
                        ),
                    },
                )
                if event.user != user:
                    event.user = user
                    event.save()
            except IntegrityError:
                ...

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created an event named {event.title} at"
                    f" {event.reminder_datetime} -about {event.category.name}"
                )
            )
        self.stdout.write(
            self.style.SUCCESS(
                f"You can access all events as '{user.username}' \n"
                f"Username: {user.username}, pasword: {user.username}"
            )
        )

    @staticmethod
    def _handle_category_names(category_names: str, user: User) -> List[EventCategory]:
        event_category_objects = []
        for name in category_names.split(","):
            category, _ = EventCategory.objects.get_or_create(
                name=name, slug=slugify(name), user=user
            )
            event_category_objects.append(category)
        else:
            category, _ = EventCategory.objects.get_or_create(
                name="Default", slug="default", user=user
            )
            event_category_objects.append(category)
        return event_category_objects
