import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from store.models import Promotion


class Command(BaseCommand):

    help = "This command creates promotions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many promotions you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_collections = Promotion.objects.all()
        seeder.add_entity(
            Promotion, number, {
                "description": lambda x: seeder.faker.company(),
                "discount": lambda x: round(random.randrange(1, 10), 2),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} promotions created!"))

