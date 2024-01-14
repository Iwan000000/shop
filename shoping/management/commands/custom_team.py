from django.core.management import BaseCommand

from shoping.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()

        list_categoryes = [
            {"name": "индейка", "description": "диетическая"},
            {"name": "телятина", "description": "диетическая"}

        ]

        list_products = [
            {
                "name": "грудинка",
                "description": "на ребре",
                "image": "",
                "category": Category.objects.get(id=1),
                "price_for_one": 339,
                "date_of_creatio": "2024-01-14",
                "last_modified_date": "2024-01-14"
            },
            {
                "name": "бекон",
                "description": "без кости",
                "image": "",
                "category": Category.objects.get(id=1),
                "price_for_one": 339,
                "date_of_creatio": "2024-01-14",
                "last_modified_date": "2024-01-14"
            },
            {
                "name": "филе грудки",
                "description": "без кости",
                "image": "",
                "category": Category.objects.get(id=3),
                "price_for_one": 420,
                "date_of_creatio": "2024-01-14",
                "last_modified_date": "2024-01-14"
            },

        ]


        for categoryes_item in list_categoryes:
            Category.objects.create(**categoryes_item)

        for products_item in list_products:
            Product.objects.create(**products_item)
