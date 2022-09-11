from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem

# ini tdd


class AnimalTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="supreme", item_price=100, item_stock=3,
                                   description="Oriiiii", rating=0, item_url="https://www.supremenewyork.com/")

    def test_katalog_name_should_be_exist(self):
        supreme = CatalogItem.objects.get(item_name="supreme", item_price=100, item_stock=3,
                                          description="Oriiiii", rating=0, item_url="https://www.supremenewyork.com/")
        self.assertEqual(supreme.item_name, "supreme")

    def test_katalog_props_should_be_same(self):
        supreme = CatalogItem.objects.get(item_name="supreme", item_price=100, item_stock=3,
                                          description="Oriiiii", rating=0, item_url="https://www.supremenewyork.com/")
        self.assertEqual(supreme.item_name, "supreme")
        self.assertEqual(supreme.item_price, 100)
        self.assertEqual(supreme.item_stock, 3)
        self.assertEqual(supreme.description, "Oriiiii")
        self.assertEqual(supreme.rating, 0)
        self.assertEqual(supreme.item_url, "https://www.supremenewyork.com/")
