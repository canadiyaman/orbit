from django.db import models
from django.utils.text import slugify

from .base_models import TimeStampModel


__all__ = ["Event", "EventCategory"]


class Event(TimeStampModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    reminder_datetime = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey("event.EventCategory", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    @property
    def date(self):
        return self.reminder_datetime.date()

    @property
    def time(self):
        return self.reminder_datetime.time()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        unique_together = ("user", "slug")
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventCategory(TimeStampModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ("user", "slug")
        verbose_name = "Event Category"
        verbose_name_plural = "Event Categories"
