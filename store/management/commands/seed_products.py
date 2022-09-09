import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from store.models import Product, Collection


class Command(BaseCommand):

    help = "This command creates products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many products you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        collections = Collection.objects.all()
        seeder.add_entity(
            Product, number, {
                'title': lambda x: seeder.faker.name(),
                'slug': lambda x: seeder.faker.paragraph(nb_sentences=number),
                'description': lambda x: seeder.faker.paragraph(nb_sentences=5),
                'unit_price': lambda x: random.randrange(5, 1000, 10),
                'inventory': lambda x: random.randrange(1, 100),
                'collection': lambda x: random.choice(collections),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} products created!"))
