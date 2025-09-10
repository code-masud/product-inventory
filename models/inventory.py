class Inventory:
    def __init__(self):
        self.products = {}

    def get_product(self, code):
        if code in self.products:
            return self.products.get(code)
        else:
            print(f"Product {code} not found.")
            return None

    def add_product(self, product):
        if product.code in self.products:
            print(f"Product {product.code} already exist.")
            return None
        else:
            self.products[product.code] = product
            print(f"Product {product.code} added successfully.")
            return product

    def remove_product(self, code):
        if code in self.products:
            remove_index = self.products.pop(code)
            print(f"Product {code} removed successfully.")
            return remove_index
        else:
            print(f"Product {code} is not found.")
            return None

    def update_product(self, code, **kwargs):
        if code in self.products:
            product = self.products[code]
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
                    print(f"Updated {key} for Product {code}.")
                else:
                    print(f"Attribute {key} not found.")
            print(f"Product {code} updated successfully.")
            return self.products[code]
        else:
            print(f"Product {code} is not found.")
            return None

    def search_product(self, term):
        found_products  = []

        if term in self.products:
            found_products.append(self.products[term])

        for product in self.products.values():
            if term.lower() in product.name.lower():
                found_products.append(product)
            elif product.category and term.lower() in product.category.name.lower():
                found_products.append(product)

        if found_products:
            return " & ".join([f"{item.name}" for item in found_products])
        else:
            return None

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products.values():
                print(product)

    def calculate_total_stock_value(self):
        return sum((float(item.price) * float(item.qty)) for item in self.products.values())