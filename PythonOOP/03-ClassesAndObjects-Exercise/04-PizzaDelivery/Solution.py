class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity
            self.price += price_per_ingredient * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                if quantity <= self.ingredients[ingredient]:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_ingredient * quantity
                return f"Please check again the desired quantity of {ingredient}!"
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {self.__ingredients_as_string()} " \
               f"and the price will be {self.price}lv."

    def __ingredients_as_string(self):
        """This method is for converting the keys and values from self.ingredients dict
        to strings which are going to be appended to list in following format:
        ingredient: quantity
        """
        result = []
        for key in self.ingredients:
            result.append(f"{key}: {self.ingredients[key]}")
        return ', '.join(result)