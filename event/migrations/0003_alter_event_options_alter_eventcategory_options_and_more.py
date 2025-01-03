# Generated by Django 5.1.2 on 2024-10-11 23:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_alter_event_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"verbose_name": "Event", "verbose_name_plural": "Events"},
        ),
        migrations.AlterModelOptions(
            name="eventcategory",
            options={"verbose_name": "Event Category", "verbose_name_plural": "Event Categories"},
        ),
        migrations.AlterField(
            model_name="eventcategory",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name="event",
            unique_together={("user", "slug")},
        ),
        migrations.AlterUniqueTogether(
            name="eventcategory",
            unique_together={("user", "slug")},
        ),
    ]
