import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from store.models import Customer


class Command(BaseCommand):

    help = "This command creates customers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many customers you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_customers = Customer.objects.all()
        seeder.add_entity(
            Customer, number, {
                "title": lambda x: seeder.faker.name()
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} customers created!"))

