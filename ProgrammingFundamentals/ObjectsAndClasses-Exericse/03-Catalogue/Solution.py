class Catalogue:
    def __init__(self,name):
        self.name = name
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def get_by_letter(self,first_letter):
        return list(filter(lambda x:x[0] == first_letter,self.products))
    def __repr__(self):
        self.products.sort()
        return f"Items in the {self.name} catalogue:\n" + "\n".join(self.products)