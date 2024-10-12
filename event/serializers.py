from datetime import datetime

from django.utils.text import slugify
from rest_framework import serializers

from .models import Event, EventCategory

__all__ = ["EventSerializer", "EventCategorySerializer"]


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]


class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)
    category_name = serializers.CharField(write_only=True)
    date = serializers.DateField()
    time = serializers.TimeField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "date",
            "time",
            "category_name",
            "category",
        ]
        read_only_fields = ["slug", "reminder_datetime", "user"]

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        request = self.context.get("request")
        data["user"] = request.user

        if "category_name" in data:
            category_name = data.pop("category_name")
            data["category"], _ = EventCategory.objects.get_or_create(
                user=request.user, name=category_name, slug=slugify(category_name)
            )

        if all(["date" in data, "time" in data]):
            date = data.pop("date")
            time = data.pop("time")
            data["reminder_datetime"] = datetime.combine(date, time)

        data["slug"] = slugify(data["title"])
        return data
