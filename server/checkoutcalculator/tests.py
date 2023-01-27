from django.test import TestCase

from .models import Item

import decimal

# Create your tests here.
class ItemModelTest(TestCase):
    databases = {"inventory"}

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name="test1", price=2.99)
        Item.objects.create(name="test2", price=2.99)
        Item.objects.create(name="test3", price=0.00)
        #Item.objects.create(name="test4", price=0.00)

    def test_name_content(self):
        item = Item.objects.get(id=1)
        self.assertEquals(item.name, "test1")

    def test_price_content(self):
        item = Item.objects.get(id=2)
        # compare strings to have fixed number of decimal places
        self.assertEquals(str(item.price), "2.99")

    def test_default_values(self):
        item = Item.objects.get(id=3)
        # compare strings to have fixed number of decimal places
        self.assertEquals(str(item.price), "0.00")
        self.assertEquals(item.taxed_item, True)  # Default value when not specified
        self.assertEquals(item.available_stock, 0)  # Default value when not specified