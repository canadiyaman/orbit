from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = "Generates initial events and categories"

    def add_arguments(self, parser):
        parser.add_argument(
            "-username", nargs="?", type=str, help="Username will use also set password"
        )

    def handle(self, *args, **options):
        username = options.get("username") or "default"

        user, _ = User.objects.get_or_create(username=username)
        user.set_password(username)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully user created username={username}, password:{username}"
            )
        )
