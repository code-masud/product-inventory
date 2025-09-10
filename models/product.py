class Product:
    def __init__(self, code, name, price, category, qty=0):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.qty = qty

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Category: {self.category.name if self.category else "N/A"}, Stock: {self.qty:,.2f}"