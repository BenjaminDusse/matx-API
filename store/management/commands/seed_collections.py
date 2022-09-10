import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from store.models import Collection, Product


class Command(BaseCommand):

    help = "This command creates collections"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many collections you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        collections = Collection.objects.all()
        products = Product.objects.all()
        seeder.add_entity(
            Collection, number, {
                "title": lambda x: seeder.faker.company(),
                # 'featured_product': lambda x: random.choice(products)
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} collections created!"))

