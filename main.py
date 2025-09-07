from category import Category
from product import Product
from inventory import Inventory

if __name__ == '__main__':
    cat1 = Category("Laptop")
    cat2 = Category("Components")

    my_inventory = Inventory()

    # Add products directly
    my_inventory.add_product(Product("L001", "Gaming Laptop", 500.0, cat1))
    my_inventory.add_product(Product("M002", "A4Tech Mouse", 50.0, cat2, 5))
    my_inventory.add_product(Product("K003", "Mechanical Keyboard", 100.0, cat2))

    print("\n--- Initial Inventory ---")
    my_inventory.display_inventory()

    print("\n--- Perform operations ---")
    # Perform all operations without intermediate display
    my_inventory.update_product("L001", price=1150.00, qty=45)
    my_inventory.remove_product("M002")
    my_inventory.update_product("K003", name="General Keyboard", qty=7)

    print("\n--- Final Inventory ---")
    my_inventory.display_inventory()

    print(f"\nTotal stock value: ${my_inventory.calculate_total_stock_value()}")

    query = 'o'
    search_result = my_inventory.search_product(query)
    print(f"Search for '{query}': {search_result}")