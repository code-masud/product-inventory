import unittest
import sys
import os
from models import Category, Product, Inventory

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestInventory(unittest.TestCase):
    def test_product_create(self):
            cat1 = Category("Laptop")
            my_inventory = Inventory()
            p1 = Product("L001", "Gaming Laptop", 500.0, cat1)
            my_inventory.add_product(p1)

            self.assertEqual(len(my_inventory.products), 1)
            self.assertEqual(my_inventory.get_product('L001'), p1)
            self.assertEqual(my_inventory.products[p1.code].category, cat1)

    def test_product_remove(self):
            cat1 = Category("Laptop")
            cat2 = Category("Components")
            p1 = Product("L001", "Gaming Laptop", 500.0, cat1)
            p2 = Product("M002", "A4Tech Mouse", 50.0, cat2, 5)

            my_inventory = Inventory()
            my_inventory.add_product(p1)
            my_inventory.add_product(p2)

            self.assertEqual(len(my_inventory.products), 2)
            self.assertEqual(my_inventory.remove_product(p2.code), p2)
            self.assertEqual(len(my_inventory.products), 1)

    def test_product_search(self):
            cat1 = Category("Laptop")
            cat2 = Category("Components")
            p1 = Product("L001", "Gaming Laptop", 500.0, cat1)
            p2 = Product("M002", "A4Tech Mouse", 50.0, cat2, 5)

            my_inventory = Inventory()
            my_inventory.add_product(p1)
            my_inventory.add_product(p2)

            self.assertEqual(my_inventory.search_product("Components"), "A4Tech Mouse")
            self.assertEqual(my_inventory.search_product("Keyboard"), None)

if __name__ == '__main__':
    unittest.main()