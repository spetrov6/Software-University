from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product_to_remove = self.find(product_name)
        if product_to_remove:
            self.products.remove(product_to_remove)

    def __repr__(self):
        products_information = ""
        for product in self.products:
            if self.products.index(product) < len(self.products) - 1:
                products_information += f"{product.name}: {product.quantity}\n"
            else:
                products_information += f"{product.name}: {product.quantity}"
        return products_information

